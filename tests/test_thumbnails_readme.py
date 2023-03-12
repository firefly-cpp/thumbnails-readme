import os
import pathlib
import shutil
from pathlib import Path

from PIL import Image
from thumbnails_readme.thumbnails_readme import (ImageThumbnail, crawl,
                                                 prepare_readme,
                                                 prepare_thumbnails_folder)

# Workaround for Windows cairosvg import error
# can use GIMP / Inkscape instead
# poppler_path = Path('C:/Program Files/poppler-0.68.0/bin')
# os.environ['path'] += r';C:/Program Files/poppler-0.68.0/bin'
# os.environ['path'] += r';C:\Program Files\GTK2-Runtime Win64\bin'


TESTFILE_README_CONTENTS = (
    """# thumbnails-readme --- Create thumbnails\n\n---"""
)

max_size = (128, 128)
pdf_quality = 15
poppler_path = None
path = os.getcwd()
path = os.path.dirname(path + "/tests")
skiplist = ("image_thumbnails",)
path_to_thumbnails_folder = Path(path + "/image_thumbnails")
path_to_readme = Path(path + "/README.md")


def test_thumbnails_folder_creation():
    try:
        os.rmdir("\\image_thumbnails")
    except:
        pass

    prepare_thumbnails_folder(path_to_thumbnails_folder)
    assert os.path.exists(path_to_thumbnails_folder) == 1


def test_readme_creation():
    TESTFILE: str = "./README.md"

    try:
        os.remove(TESTFILE)
    except:
        pass

    with open(TESTFILE, "w", encoding="utf-8") as filewrite:
        filewrite.write(TESTFILE_README_CONTENTS)
        filewrite.flush()

    assert os.path.exists("./README.md") == 1


def test_readme_preparation():
    prepare_readme("./README.md")
    with open("./README.md", "r") as readme:
        contents = readme.read()
        assert contents == TESTFILE_README_CONTENTS


def test_create_png_image():
    image = Image.new("RGB", (128, 128))
    image.save("examplefile.png", "PNG")
    assert os.path.exists("./examplefile.png") == 1


def test_create_jpg_image():
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
        max_size,
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
        max_size,
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
        max_size,
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
        max_size,
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


def test_animate_pdf_image():
    file = "example-long.pdf"
    image = ImageThumbnail(
        Path(path),
        os.path.splitext(file)[0],
        os.path.splitext(file)[1],
        max_size,
        pdf_quality,
    )

    relative_path = str(image.path_to_file).replace(path, "")
    relative_path = pathlib.Path(relative_path)
    relative_path = str(pathlib.Path(*relative_path.parts[1:]))

    readme_line = (
        "[!["
        + image.file_name
        + "](/image_thumbnails/"
        + "pdf_animation_"
        + image.file_name
        + ".gif"
        + ")]("
        + relative_path
        + "/"
        + image.file_name
        + image.file_extension
        + ")\n"
    )

    assert (
        str(readme_line)
        == "[![example-long](/image_thumbnails/pdf_animation_example-long.gif)](./example-long.pdf)\n"
    )


def test_crawl():
    crawl(
        path,
        path_to_readme,
        path_to_thumbnails_folder,
        max_size,
        pdf_quality,
        skiplist,
        poppler_path=None,
    )
    assert os.path.exists("./README.md") == 1

    with open("./README.md", "r") as readme:
        readme_lines = readme.readlines()
        assert any(
            "# thumbnails-readme --- Create thumbnails" in line
            for line in readme_lines
        )
        assert any("\n" in line for line in readme_lines)
        assert any("---" in line for line in readme_lines)
        assert any("# Thumbnails" in line for line in readme_lines)
        assert any(
            "[![example-long](/image_thumbnails/pdf_animation_example-long.gif)](tests/example-long.pdf)"
            or "[![example-long](/image_thumbnails/pdf_animation_example-long.gif)](example-long.pdf)"
            in line
            for line in readme_lines
        )
        assert any(
            "[![example-pdf](/image_thumbnails/pdf_example-pdf_thumb.png)](tests/example-pdf.pdf)"
            or "[![example-pdf](/image_thumbnails/pdf_example-pdf_thumb.png)](example-pdf.pdf)"
            in line
            for line in readme_lines
        )
        assert any(
            "[![example-svg](/image_thumbnails/svg_example-svg_thumb.png)](tests/example-svg.svg)"
            or "[![example-svg](/image_thumbnails/svg_example-svg_thumb.png)](example-svg.svg)"
            in line
            for line in readme_lines
        )
        assert any(
            "[![examplefile](/image_thumbnails/png_examplefile_thumb.png)](examplefile.png)"
            in line
            for line in readme_lines
        )
        assert any(
            "[![examplefile](/image_thumbnails/jpg_examplefile_thumb.png)](examplefile.jpg)"
            in line
            for line in readme_lines
        )


def test_cleanup():
    os.remove("./examplefile.png")
    assert os.path.exists("./examplefile.png") == 0
    os.remove("./examplefile.jpg")
    assert os.path.exists("./examplefile.jpg") == 0
    shutil.rmtree(path_to_thumbnails_folder)
    assert os.path.exists(path_to_thumbnails_folder) == 0
    os.remove("./README.md")

    assert os.path.exists("./README.md") == 0
    assert os.path.exists("./image_thumbnails/jpg_examplefile_thumb.png") == 0
    assert (
        os.path.exists("./image_thumbnails/pdf_animation_example-long.gif")
        == 0
    )
    assert os.path.exists("./image_thumbnails/pdf_example-pdf_thumb.png") == 0
    assert os.path.exists("./image_thumbnails/png_examplefile_thumb.png") == 0
    assert os.path.exists("./image_thumbnails/svg_example-svg_thumb.png") == 0
