"""Test thumbnails_readme.py."""

import contextlib
import pathlib
import shutil
from pathlib import Path

from PIL import Image

from thumbnails_readme.thumbnails_readme import (
    ImageThumbnail,
    crawl,
    prepare_readme,
    prepare_thumbnails_folder,
)

# Workaround for Windows cairosvg import error
# can use GIMP / Inkscape instead


TESTFILE_README_CONTENTS = (
    """# thumbnails-readme --- Create thumbnails\n\n---"""
)

max_size = (128, 128)
pdf_quality = 15
# Windows
# poppler_path = Path(r'C:\Program Files\poppler-0.68.0\bin')
# Linux
poppler_path = None
path = Path.cwd()
path_str = (path / 'tests')
path = Path(path_str).parent
skiplist = ('image_thumbnails',)
path_to_thumbnails_folder = Path(path / 'image_thumbnails')
path_to_readme = Path(path / 'README.md')




def test_thumbnails_folder_creation() -> None:
    """Test creation of thumbnails folder."""
    with contextlib.suppress(Exception):
        Path.rmdir(Path('\\image_thumbnails'))

    prepare_thumbnails_folder(Path(path_to_thumbnails_folder))
    assert Path.exists(Path(path_to_thumbnails_folder)) == 1


def test_readme_creation() -> None:
    """Test creation of README.md file."""
    testfile: str = './README.md'

    with contextlib.suppress(Exception):
        Path.unlink(Path(testfile))

    with Path(testfile).open('w', encoding='utf-8') as filewrite:
        filewrite.write(TESTFILE_README_CONTENTS)
        filewrite.flush()

    assert Path.exists(Path('./README.md')) == 1


def test_readme_preparation() -> None:
    """Test preparation of README.md file."""
    prepare_readme(Path('./README.md'))
    with Path('./README.md').open('r') as readme:
        contents = readme.read()
        print("\n")
        print(contents)
        print(TESTFILE_README_CONTENTS)
        assert contents == TESTFILE_README_CONTENTS


def test_create_png_image() -> None:
    """Test creation of PNG thumbnail."""
    image = Image.new('RGB', (128, 128))
    image.save('examplefile.png', 'PNG')
    assert Path.exists(Path('./examplefile.png')) == 1


def test_create_jpg_image() -> None:
    """Test creation of JPG thumbnail."""
    image = Image.new('RGB', (128, 128))
    image.save('examplefile.jpg', 'JPEG')
    assert Path.exists(Path('./examplefile.jpg')) == 1


# Test default png, works with different extensions: jpg, svg, pdf
def test_png_image() -> None:
    """Test creation of PNG thumbnail."""
    file = 'example.png'
    image = ImageThumbnail(
        Path(path),
        Path(file).stem,
        Path(file).suffix,
        max_size,
        pdf_quality,
    )
    readme_line = (
            '!['
            + pathlib.PurePath(image.path_to_file).parent.name
            + image.file_name
            + '](/image_thumbnails/'
            + image.file_extension.split('.')[-1].lower()
            + '_'
            + image.file_name
            + '_thumb.png'
            + ')\r\n'
    )
    assert (
            str(readme_line)
            == '!['
            + pathlib.PurePath(image.path_to_file).parent.name
            + 'example](/image_thumbnails/png_example_thumb.png)\r\n'
    )


def test_jpg_image() -> None:
    """Test creation of JPG thumbnail."""
    file = 'example.jpg'
    image = ImageThumbnail(
        Path(path),
        Path(file).stem,
        Path(file).suffix,
        max_size,
        pdf_quality,
    )
    readme_line = (
            '!['
            + pathlib.PurePath(image.path_to_file).parent.name
            + image.file_name
            + '](/image_thumbnails/'
            + image.file_extension.split('.')[-1].lower()
            + '_'
            + image.file_name
            + '_thumb.png'
            + ')\r\n'
    )
    assert (
            str(readme_line)
            == '!['
            + pathlib.PurePath(image.path_to_file).parent.name
            + 'example](/image_thumbnails/jpg_example_thumb.png)\r\n'
    )


def test_svg_image() -> None:
    """Test creation of SVG thumbnail."""
    file = 'example.svg'
    image = ImageThumbnail(
        Path(path),
        Path(file).stem,
        Path(file).suffix,
        max_size,
        pdf_quality,
    )
    readme_line = (
            '!['
            + pathlib.PurePath(image.path_to_file).parent.name
            + image.file_name
            + '](/image_thumbnails/'
            + image.file_extension.split('.')[-1].lower()
            + '_'
            + image.file_name
            + '_thumb.png'
            + ')\r\n'
    )
    assert (
            str(readme_line)
            == '!['
            + pathlib.PurePath(image.path_to_file).parent.name
            + 'example](/image_thumbnails/svg_example_thumb.png)\r\n'
    )


def test_pdf_image() -> None:
    """Test creation of PDF thumbnail."""
    file = 'example.pdf'
    image = ImageThumbnail(
        Path(path),
        Path(file).stem,
        Path(file).suffix,
        max_size,
        pdf_quality,
    )
    readme_line = (
            '!['
            + pathlib.PurePath(image.path_to_file).parent.name
            + image.file_name
            + '](/image_thumbnails/'
            + image.file_extension.split('.')[-1].lower()
            + '_'
            + image.file_name
            + '_thumb.png'
            + ')\r\n'
    )
    assert (
            str(readme_line)
            == '!['
            + pathlib.PurePath(image.path_to_file).parent.name
            + 'example](/image_thumbnails/pdf_example_thumb.png)\r\n'
    )


def test_animate_pdf_image() -> None:
    """Test animated PDF thumbnail."""
    file = Path('example-long.pdf')
    image = ImageThumbnail(
        Path(path),
        Path(file).stem,
        Path(file).suffix,
        max_size,
        pdf_quality,
    )

    relative_path = str(image.path_to_file).replace(str(path), '')
    relative_path = pathlib.Path(relative_path)
    relative_path = str(pathlib.Path(*relative_path.parts[1:]))

    readme_line = (
            '[!['
            + str(image.file_name)
            + '](/image_thumbnails/'
            + 'pdf_animation_'
            + str(image.file_name)
            + '.gif'
            + ')]('
            + relative_path
            + '/'
            + str(image.file_name)
            + str(image.file_extension)
            + ')\n'
    )

    assert (
            str(readme_line)
            == '[![example-long](/image_thumbnails/'
               'pdf_animation_example-long.gif)]'
               '(./example-long.pdf)\n'
    )


def test_crawl() -> None:
    """Test crawl function."""
    crawl(
        path,
        path_to_readme,
        path_to_thumbnails_folder,
        max_size,
        pdf_quality,
        skiplist,
        poppler_path=poppler_path,
    )
    assert Path.exists(Path('./README.md')) == 1

    with Path('./README.md').open() as readme:
        readme_lines = readme.readlines()
        assert any(
            '# thumbnails-readme --- Create thumbnails' in line
            for line in readme_lines
        )
        assert any('\n' in line for line in readme_lines)
        assert any('---' in line for line in readme_lines)
        assert any('# Thumbnails' in line for line in readme_lines)
        assert any(
            '[![example-long](/image_thumbnails/pdf_animation_example-long.gif)](tests/example-long.pdf)'
            for line in readme_lines
        )
        assert any(
            '[![example-pdf](/image_thumbnails/pdf_example-pdf_thumb.png)](tests/example-pdf.pdf)'
            for line in readme_lines
        )
        assert any(
            '[![example-svg](/image_thumbnails/svg_example-svg_thumb.png)](tests/example-svg.svg)'
            for line in readme_lines
        )
        assert any(
            '[![examplefile](/image_thumbnails/png_examplefile_thumb.png)](examplefile.png)'
            in line
            for line in readme_lines
        )
        assert any(
            '[![examplefile](/image_thumbnails/jpg_examplefile_thumb.png)](examplefile.jpg)'
            in line
            for line in readme_lines
        )


def test_cleanup() -> None:
    """Cleanup after tests."""
    Path.unlink(Path('./examplefile.png'))
    assert Path.exists(Path('./examplefile.png')) == 0
    Path.unlink(Path('./examplefile.jpg'))
    assert Path.exists(Path('./examplefile.jpg')) == 0
    shutil.rmtree(path_to_thumbnails_folder)
    assert Path.exists(Path(path_to_thumbnails_folder)) == 0
    Path.unlink(Path('./README.md'))

    assert Path.exists(Path('./README.md')) == 0
    assert Path.exists(
        Path('./image_thumbnails/jpg_examplefile_thumb.png')) == 0
    assert (
            Path.exists(Path('./image_thumbnails/pdf_animation_example-long.gif'))
            == 0)

    assert Path.exists(
        Path('./image_thumbnails/pdf_example-pdf_thumb.png')) == 0
    assert Path.exists(
        Path('./image_thumbnails/png_examplefile_thumb.png')) == 0
    assert Path.exists(
        Path('./image_thumbnails/svg_example-svg_thumb.png')) == 0
