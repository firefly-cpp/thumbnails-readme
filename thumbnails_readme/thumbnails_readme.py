"""Create thumbnails for all images in the folders, write to README.md."""

import contextlib
import glob
import os
import pathlib
import shutil
from pathlib import Path
from urllib.error import HTTPError

import cairosvg
from pdf2image import convert_from_path
from PIL import Image


class ImageThumbnail:
    """Class for the image."""

    def __init__(
            self: 'ImageThumbnail',
            path_to_file: Path,
            file_name: Path,
            file_extension: Path,
            max_size: tuple,
            pdf_quality: int,
    ) -> None:
        """Initialize the class."""
        self.path_to_file = path_to_file
        self.file_name = file_name
        self.file_extension = file_extension
        self.max_size = max_size  # tuple
        self.pdf_quality = pdf_quality

    def create_raster_thumbnail(self: 'ImageThumbnail',
                                path_to_thumbnails_folder: Path,
                                ) -> None:
        """Create thumbnail for the raster image."""
        new_file_name = self.file_name + '_thumb.png'
        # Pillow - Python Imaging Library to work with png and jpg
        im = Image.open(self.path_to_file)
        im.thumbnail(self.max_size)
        im.save(
            f"{path_to_thumbnails_folder}"
            f"/{self.file_extension.split('.')[-1].lower()}_{new_file_name}",
        )

    def create_pdf_thumbnail(
            self: 'ImageThumbnail',
            path_to_thumbnails_folder: Path,
            poppler_path: Path,
            readme,
            path: Path,
    ) -> None:
        """Create thumbnail for the PDF."""
        if os.name == 'nt':
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
                self.path_to_file, self.pdf_quality, size=self.max_size[0],
            )
        # If there is more than one page in the PDF, create an animation
        if len(images) > 1:
            # Create a thumbnail for each page in the PDF
            for image in images:
                # Save each image as png
                image.save(
                    f'{path_to_thumbnails_folder}'
                    f'/pdf_to_gif_image_{self.file_name}{images.index(image) + 1}_thumb.png',
                )
            # Create glob regex pattern for created pdf--> png images
            file_pattern_input = (f'{path_to_thumbnails_folder}'
                                  f'/pdf_to_gif_image_{self.file_name}*_thumb.png')
            file_pattern_output = (f'{path_to_thumbnails_folder}'
                                   f'/pdf_animation_{self.file_name}.gif')

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
                    format='GIF',
                    save_all=True,
                    duration=1000,
                    loop=0,
                    size=self.max_size[0],
                )

                # Write to README.md
                self.write_to_readme(readme, path, True)

            # Remove all the png thumb images for animation
            for png_images in glob.glob(file_pattern_input):
                Path.unlink(Path(png_images))
        else:
            for image in images:
                image.save(
                    f'{path_to_thumbnails_folder}'
                    f'/pdf_{self.file_name}_thumb.png',
                )
                self.write_to_readme(readme, path)

    def create_svg_thumbnail(self: 'ImageThumbnail',
                             path_to_thumbnails_folder: Path,
                             ) -> None:
        """Create thumbnail for the SVG cairosvg library."""
        cairosvg.svg2png(
            url=str(self.path_to_file),
            output_width=self.max_size[0],
            output_height=self.max_size[1],
            write_to=f'{path_to_thumbnails_folder}'
                     f'/svg_{self.file_name}_thumb.png',
        )

    def write_to_readme(self: 'ImageThumbnail',
                        readme,
                        path: Path,
                        animated: bool = False) -> None:
        """Write to README.md.

        Create a link that opens the
        original image around thumbnails
        image that is showed in the README.md
        file. The boolean Animated is used
        to distinguish between multipage
        PDFs since their thumbnails
        are animated and files are
        named differently.
        """
        relative_path = str(self.path_to_file).replace(str(path), '')
        relative_path = pathlib.Path(relative_path)
        relative_path = str(pathlib.Path(*relative_path.parts[1:]))
        if not animated:
            readme.write(
                '[!['
                + self.file_name
                + '](/image_thumbnails/'
                + self.file_extension.split('.')[-1].lower()
                + '_'
                + self.file_name
                + '_thumb.png'
                + ')]('
                + relative_path
                + ')\n',
            )
        else:
            readme.write(
                '[!['
                + str(self.file_name)
                + '](/image_thumbnails/'
                + 'pdf_animation_'
                + str(self.file_name)
                + '.gif'
                + ')]('
                + relative_path
                + ')\n',
            )


# Prepare README.md file - remove old content
def prepare_readme(path_to_readme: Path) -> None:
    """Remove old content in upcoming package version.

    remove "# Generated Thumbnails".
    """
    lines_for_removal = ['# Generated Thumbnails',
                         '# Thumbnails',
                         '(/image_thumbnails/']
    path_to_readme_temp = (
            Path(path_to_readme).stem + '_temp' + Path(path_to_readme).suffix
    )
    # Create a temporary README.md file
    Path.touch(Path(path_to_readme_temp))

    with Path(path_to_readme).open('r') as readme, Path(
            path_to_readme_temp).open('w') as readme_two:
        for line in readme:
            if not any(
                    remove_line in line for remove_line in lines_for_removal
            ):
                readme_two.write(line)
        readme.close()
        readme_two.close()
        Path.unlink(Path(path_to_readme))
        Path.rename(Path(path_to_readme_temp), path_to_readme)


# Create image_thumbnails folder if it doesn't exist
def prepare_thumbnails_folder(path_to_thumbnails_folder: Path) -> None:
    """Create image_thumbnails folder if it doesn't exist."""
    if not Path.exists(path_to_thumbnails_folder):
        Path.mkdir(path_to_thumbnails_folder, parents=True)
    else:
        shutil.rmtree(path_to_thumbnails_folder)
        Path.mkdir(path_to_thumbnails_folder, parents=True)


# Create thumbnails for all images in the folders, write to README.md
def crawl(
        path: Path,
        path_to_readme: Path,
        path_to_thumbnails_folder: Path,
        max_size: tuple,
        pdf_quality: int,
        skiplist: tuple,
        poppler_path: None or Path = None,
) -> None:
    """Create thumbnails for all images in the folders, write to README.md."""
    # Supported image formats
    all_supported_formats = [
        '.bmp',
        '.gif',
        '.ico',
        'jpeg',
        '.jpg',
        '.png',
        '.tga',
        '.tiff',
        '.webp',
        '.pdf',
        '.svg',
    ]
    # Supported raster image formats
    supported_raster_formats = [
        '.bmp',
        '.gif',
        '.ico',
        'jpeg',
        '.jpg',
        '.png',
        '.tga',
        '.tiff',
        '.webp',
    ]
    # Open the file README.md and read the content
    # "a" to allow reading and writing
    with Path(path_to_readme).open('a') as readme:
        # Write TITLE # Thumbnails to the README.md file
        readme.write('\n# Thumbnails\n')

        # Loop through all files and folders in the current directory
        for root, directory, files in os.walk(path, topdown=True):
            directory[:] = [d for d in directory if d not in skiplist]
            # For all image files in directory
            for file in files:
                # ignore files that are not images
                if (
                        pathlib.Path(file).suffix.lower()
                        not in all_supported_formats
                ):
                    continue
                # Create ImageThumbnail object
                image = ImageThumbnail(
                    Path(root + '/' + file),
                    pathlib.Path(file).stem,
                    pathlib.Path(file).suffix,
                    max_size,
                    pdf_quality,
                )
                if image.file_extension.lower() in supported_raster_formats:
                    image.create_raster_thumbnail(path_to_thumbnails_folder)
                    image.write_to_readme(readme, path)

                elif image.file_extension.lower() in ['.pdf']:
                    image.create_pdf_thumbnail(
                        path_to_thumbnails_folder, poppler_path, readme, path,
                    )

                elif image.file_extension.lower() in ['.svg']:
                    try:
                        image.create_svg_thumbnail(path_to_thumbnails_folder)
                        image.write_to_readme(readme, path)
                    except HTTPError:
                        print(
                            'HTTPError: Check if the SVG file is valid and '
                            'accessible, file ' + str(image.path_to_file),
                        )
                        continue
