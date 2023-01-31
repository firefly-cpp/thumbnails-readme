import os
import pathlib
import shutil
from pathlib import Path

from pdf2image import convert_from_path
from PIL import Image
import cairosvg

class ImageThumbnail:
    """
    Class for the image
    """

    def __init__(self, path_to_file, file_name, file_extension, max_size, pdf_quality):
        """
        Default constructor
        """
        self.path_to_file = path_to_file
        self.file_name = file_name
        self.file_extension = file_extension
        self.max_size = max_size
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

    def create_pdf_thumbnail(self, path_to_thumbnails_folder, poppler_path):
        """
        Create thumbnail for the PDF
        """
        if os.name == "nt":
            # Windows - poppler path required
            images = convert_from_path(
                self.path_to_file,
                self.pdf_quality,
                poppler_path=poppler_path,
                size=self.max_size[0],
            )
        else:
            # Linux - sudo apt-get install poppler-utils
            images = convert_from_path(
                self.path_to_file, self.pdf_quality, size=self.max_size[0]
            )
        for image in images:
            image.save(
                f"{path_to_thumbnails_folder}" f"/pdf_{self.file_name}_thumb.png"
            )

    def create_svg_thumbnail(self, path_to_thumbnails_folder):
        """
        Create thumbnail for the SVG
        """
        cairosvg.svg2png(
            url=str(self.path_to_file),
            output_width=self.max_size[0],
            output_height=self.max_size[1],
            write_to=f"{path_to_thumbnails_folder}" f"/svg_{self.file_name}_thumb.png",
        )

    def write_to_readme(self, readme):
        """
        Write to README.md
        Create a link that opens the
        original image around thumbnails
        image that is showed in the README.md
        """
        readme.write(
            "[!["
            + pathlib.PurePath(self.path_to_file).parent.name
            + self.file_name
            + "](/image_thumbnails/"
            + self.file_extension.split(".")[-1].lower()
            + "_"
            + self.file_name
            + "_thumb.png"
            + ")]("
            + pathlib.PurePath(self.path_to_file).parent.name
            + "/"
            + self.file_name
            + self.file_extension
            +")\n"
        )


# Prepare README.md file - remove old content
def prepare_readme(path_to_readme):
    lines_for_removal = ["# Generated Thumbnails", "(/image_thumbnails/"]
    split_filename_extension = os.path.splitext(path_to_readme)
    path_to_readme_temp = (
        split_filename_extension[0] + "_temp" + split_filename_extension[1]
    )

    with open(path_to_readme) as readme, open(path_to_readme_temp, "w") as readme_two:
        for line in readme:
            if not any(remove_line in line for remove_line in lines_for_removal):
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
    # a+ to allow reading and writing
    with open(path_to_readme, "a") as readme:
        # Write TITLE # Generated Thumbnails  to the README.md file
        readme.write("\n# Generated Thumbnails\n")

        # Loop through all files and folders in the current directory
        for root, directory, files in os.walk(path, topdown=True):
            directory[:] = [d for d in directory if d not in skiplist]
            # ignore root files
            if root == os.path.dirname(path):
                continue
            # JPG, PNG for files in directory
            for file in files:
                image = ImageThumbnail(
                    Path(root + "/" + file),
                    os.path.splitext(file)[0],
                    os.path.splitext(file)[1],
                    MAX_SIZE,
                    pdf_quality,
                )
                if image.file_extension.lower() in [".jpg", ".jpeg", ".png", ".gif"]:
                    image.create_raster_thumbnail(path_to_thumbnails_folder)
                elif image.file_extension.lower() in [".pdf"]:
                    image.create_pdf_thumbnail(path_to_thumbnails_folder, poppler_path)
                elif image.file_extension.lower() in [".svg"]:
                    image.create_svg_thumbnail(path_to_thumbnails_folder)
                if image.file_extension.lower() in [
                    ".jpg",
                    ".jpeg",
                    ".png",
                    ".gif",
                    ".pdf",
                    ".svg",
                ]:
                    image.write_to_readme(readme)