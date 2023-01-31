import os
import pathlib
from pathlib import Path

from PIL import Image
from thumbnails_readme import __version__
from thumbnails_readme.thumbnails_readme import (
    ImageThumbnail,
    prepare_readme,
    prepare_thumbnails_folder,
)

# Workaround for Windows cairosvg import error
# can use GIMP / Inkscape instead
# os.environ["path"] += r";C:\Program Files\UniConvertor-2.0rc5\dlls"

TESTFILE_CONTENTS_BEFORE = """# thumbnails-readme --- Create thumbnails\n\n---"""

MAX_SIZE = (128, 128)
pdf_quality = 15
poppler_path = None
path = os.getcwd()
path = os.path.dirname(path + "/tests")
skiplist = ("image_thumbnails",)
path_to_thumbnails_folder = Path(path + "/image_thumbnails")
path_to_readme = Path(path + "/___README.md")


def test_version():
    assert __version__ == "0.2.2"


def test_thumbnails_folder_creation():
    try:
        os.rmdir("\\image_thumbnails")
    except:
        pass

    prepare_thumbnails_folder(".\\image_thumbnails")
    assert os.path.exists(".\\image_thumbnails") == 1
    os.rmdir(".\\image_thumbnails")
    assert os.path.exists(".\\image_thumbnails") == 0


def test_readme_creation():
    TESTFILE: str = "___README.md"

    try:
        os.remove(TESTFILE)
    except:
        pass

    with open(TESTFILE, "w", encoding="utf-8") as filewrite:
        filewrite.write(TESTFILE_CONTENTS_BEFORE)
        filewrite.flush()

    assert os.path.exists("./___README.md") == 1

def test_readme_preparation():
    prepare_readme("./___README.md")
    with open("./___README.md", "r") as readme:
        contents = readme.read()
        assert contents == TESTFILE_CONTENTS_BEFORE


def create_png_image():
    image = Image.new("RGB", (128, 128))
    image.save("examplefile.png", "PNG")
    assert os.path.exists("./examplefile.png") == 1


def create_jpg_image():
    image = Image.new("RGB", (128, 128))
    image.save("examplefile.jpg", "JPEG")
    assert os.path.exists("./examplefile.jpg") == 1


# Test default png, works with different extensions: jpg, svg, pdf
def test_png_image():
    file = "example.png"
    image = ImageThumbnail(
        Path(path),
        os.path.splitext(file)[0],
        os.path.splitext(file)[1],
        MAX_SIZE,
        pdf_quality,
    )
    readme_line = (
        "!["
        + pathlib.PurePath(image.path_to_file).parent.name
        + image.file_name
        + "](/image_thumbnails/"
        + image.file_extension.split(".")[-1].lower()
        + "_"
        + image.file_name
        + "_thumb.png"
        + ")\r\n"
    )
    assert (
        str(readme_line)
        == "!["
        + pathlib.PurePath(image.path_to_file).parent.name
        + "example](/image_thumbnails/png_example_thumb.png)\r\n"
    )


def test_jpg_image():
    file = "example.jpg"
    image = ImageThumbnail(
        Path(path),
        os.path.splitext(file)[0],
        os.path.splitext(file)[1],
        MAX_SIZE,
        pdf_quality,
    )
    readme_line = (
        "!["
        + pathlib.PurePath(image.path_to_file).parent.name
        + image.file_name
        + "](/image_thumbnails/"
        + image.file_extension.split(".")[-1].lower()
        + "_"
        + image.file_name
        + "_thumb.png"
        + ")\r\n"
    )
    assert (
        str(readme_line)
        == "!["
        + pathlib.PurePath(image.path_to_file).parent.name
        + "example](/image_thumbnails/jpg_example_thumb.png)\r\n"
    )


def test_svg_image():
    file = "example.svg"
    image = ImageThumbnail(
        Path(path),
        os.path.splitext(file)[0],
        os.path.splitext(file)[1],
        MAX_SIZE,
        pdf_quality,
    )
    readme_line = (
        "!["
        + pathlib.PurePath(image.path_to_file).parent.name
        + image.file_name
        + "](/image_thumbnails/"
        + image.file_extension.split(".")[-1].lower()
        + "_"
        + image.file_name
        + "_thumb.png"
        + ")\r\n"
    )
    assert (
        str(readme_line)
        == "!["
        + pathlib.PurePath(image.path_to_file).parent.name
        + "example](/image_thumbnails/svg_example_thumb.png)\r\n"
    )


def test_pdf_image():
    file = "example.pdf"
    image = ImageThumbnail(
        Path(path),
        os.path.splitext(file)[0],
        os.path.splitext(file)[1],
        MAX_SIZE,
        pdf_quality,
    )
    readme_line = (
        "!["
        + pathlib.PurePath(image.path_to_file).parent.name
        + image.file_name
        + "](/image_thumbnails/"
        + image.file_extension.split(".")[-1].lower()
        + "_"
        + image.file_name
        + "_thumb.png"
        + ")\r\n"
    )
    assert (
        str(readme_line)
        == "!["
        + pathlib.PurePath(image.path_to_file).parent.name
        + "example](/image_thumbnails/pdf_example_thumb.png)\r\n"
    )


def cleanup():
    os.remove("./examplefile.png")
    assert os.path.exists("./examplefile.png") == 0
    os.remove("./examplefile.jpg")
    assert os.path.exists("./examplefile.jpg") == 0
    os.remove("./___README.md")
    assert os.path.exists("./___README.md") == 0


# Due to windows path issues, the tests are not run on windows
# To test locally on windows, uncomment the following lines
"""
if __name__ == "__main__":
    test_version()
    test_thumbnails_folder_creation()
    test_readme_creation()

    test_readme_preparation()

    create_png_image()
    create_jpg_image()

    test_png_image()
    test_jpg_image()
    test_svg_image()
    test_pdf_image()
"""
