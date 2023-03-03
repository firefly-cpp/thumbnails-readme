import contextlib
import glob
import os
import pathlib
import shutil
from pathlib import Path

import cairosvg
from pdf2image import convert_from_path
from PIL import Image


class ImageThumbnail:
    """
    Class for the image
    """

    def __init__(
        self, path_to_file, file_name, file_extension, max_size, pdf_quality
    ):
        """
        Default constructor
        """
        self.path_to_file = path_to_file
        self.file_name = file_name
        self.file_extension = file_extension
        self.max_size = max_size  # Tuple
        self.pdf_quality = pdf_quality

    def create_raster_thumbnail(self, path_to_thumbnails_folder):
        """
        Create thumbnail for the raster image
        """
        new_file_name = self.file_name + "_thumb.png"
        # Pillow - Python Imaging Library to work with png and jpg
        im = Image.open(self.path_to_file)
        im.thumbnail(self.max_size)
        im.save(
            f"{path_to_thumbnails_folder}"
            f"/{self.file_extension.split('.')[-1].lower()}_{new_file_name}"
        )

    def create_pdf_thumbnail(
        self, path_to_thumbnails_folder, poppler_path, readme, path
    ):
        """
        Create thumbnail for the PDF
        """
        if os.name == "nt":
            # Windows - poppler path required
            images = convert_from_path(
                pdf_path=self.path_to_file,
                dpi=self.pdf_quality,
                poppler_path=poppler_path,
                size=self.max_size[0],
            )
        else:
            # Linux - sudo apt-get install poppler-utils
            images = convert_from_path(
                self.path_to_file, self.pdf_quality, size=self.max_size[0]
            )
        # If there is more than one page in the PDF, create an animation
        if len(images) > 1:
            # Create a thumbnail for each page in the PDF
            for image in images:
                # Save each image as png
                image.save(
                    f"{path_to_thumbnails_folder}"
                    f"/pdf_to_gif_image_{self.file_name}{images.index(image)+1}_thumb.png"
                )
            # Create glob regex pattern for created pdf--> png images
            file_pattern_input = f"{path_to_thumbnails_folder}/pdf_to_gif_image_{self.file_name}*_thumb.png"
            file_pattern_output = f"{path_to_thumbnails_folder}/pdf_animation_{self.file_name}.gif"

            with contextlib.ExitStack() as stack:
                # Load images by globbing - file pattern and sort
                png_images = (
                    stack.enter_context(Image.open(f))
                    for f in sorted(glob.glob(file_pattern_input))
                )

                # Extract first image from iterator
                png_image = next(png_images)

                png_image.save(
                    fp=file_pattern_output,
                    append_images=png_images,
                    format="GIF",
                    save_all=True,
                    duration=1000,
                    loop=0,
                    size=self.max_size[0],
                )

                # Write to README.md
                self.write_to_readme(readme, path, True)

            # Remove all the png thumb images for animation
            for png_images in glob.glob(file_pattern_input):
                os.remove(png_images)
        else:
            for image in images:
                image.save(
                    f"{path_to_thumbnails_folder}"
                    f"/pdf_{self.file_name}_thumb.png"
                )
                self.write_to_readme(readme, path)

    def create_svg_thumbnail(self, path_to_thumbnails_folder):
        """
        Create thumbnail for the SVG
        Call cairosvg library
        """
        cairosvg.svg2png(
            url=str(self.path_to_file),
            output_width=self.max_size[0],
            output_height=self.max_size[1],
            write_to=f"{path_to_thumbnails_folder}"
            f"/svg_{self.file_name}_thumb.png",
        )

    def write_to_readme(self, readme, path, animated=False):
        """
        Write to README.md
        Create a link that opens the
        original image around thumbnails
        image that is showed in the README.md
        file. The boolean Animated is used
        to distinguish between multipage
        PDFs since their thumbnails
        are animated and files are
        named differently
        """

        relative_path = str(self.path_to_file).replace(path, "")
        relative_path = pathlib.Path(relative_path)
        relative_path = str(pathlib.Path(*relative_path.parts[1:]))
        if not animated:
            readme.write(
                "[!["
                + self.file_name
                + "](/image_thumbnails/"
                + self.file_extension.split(".")[-1].lower()
                + "_"
                + self.file_name
                + "_thumb.png"
                + ")]("
                + relative_path
                + ")\n"
            )
        else:
            readme.write(
                "[!["
                + self.file_name
                + "](/image_thumbnails/"
                + "pdf_animation_"
                + self.file_name
                + ".gif"
                + ")]("
                + relative_path
                + ")\n"
            )


# Prepare README.md file - remove old content
def prepare_readme(path_to_readme):
    lines_for_removal = ["# Generated Thumbnails", "(/image_thumbnails/"]
    split_filename_extension = os.path.splitext(path_to_readme)
    path_to_readme_temp = (
        split_filename_extension[0] + "_temp" + split_filename_extension[1]
    )

    with open(path_to_readme) as readme, open(
        path_to_readme_temp, "w"
    ) as readme_two:
        for line in readme:
            if not any(
                remove_line in line for remove_line in lines_for_removal
            ):
                readme_two.write(line)
        readme.close()
        readme_two.close()
        os.remove(path_to_readme)
        os.rename(path_to_readme_temp, path_to_readme)


# Create image_thumbnails folder if it doesn't exist
def prepare_thumbnails_folder(path_to_thumbnails_folder):
    if not os.path.exists(path_to_thumbnails_folder):
        os.makedirs(path_to_thumbnails_folder)
    else:
        shutil.rmtree(path_to_thumbnails_folder)
        os.makedirs(path_to_thumbnails_folder)


# Create thumbnails for all images in the folders, write to README.md
def crawl(
    path,
    path_to_readme,
    poppler_path,
    path_to_thumbnails_folder,
    MAX_SIZE,
    pdf_quality,
    skiplist,
):
    # Open the file README.md and read the content
    # "a" to allow reading and writing
    with open(path_to_readme, "a") as readme:
        # Write TITLE # Generated Thumbnails to the README.md file
        readme.write("\n# Generated Thumbnails\n")

        # Loop through all files and folders in the current directory
        for root, directory, files in os.walk(path, topdown=True):
            directory[:] = [d for d in directory if d not in skiplist]
            # For all image files in directory
            for file in files:
                # ignore files that are not images
                if os.path.splitext(file)[1].lower() not in [".jpg", "jpeg", ".png", ".gif", ".bmp", ".pdf", ".svg"]:
                    continue
                # Create ImageThumbnail object
                image = ImageThumbnail(
                    Path(root + "/" + file),
                    os.path.splitext(file)[0],
                    os.path.splitext(file)[1],
                    MAX_SIZE,
                    pdf_quality,
                )
                if image.file_extension.lower() in [
                    ".jpg",
                    ".jpeg",
                    ".png",
                    ".gif",
                    ".bmp",
                ]:
                    image.create_raster_thumbnail(path_to_thumbnails_folder)
                    image.write_to_readme(readme, path)
                elif image.file_extension.lower() in [".pdf"]:
                    image.create_pdf_thumbnail(
                        path_to_thumbnails_folder, poppler_path, readme, path
                    )
                elif image.file_extension.lower() in [".svg"]:
                    image.create_svg_thumbnail(path_to_thumbnails_folder)
                    image.write_to_readme(readme, path)
