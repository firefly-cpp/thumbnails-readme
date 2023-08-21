"""Example for thumbnails_readme.py."""

# Linux - sudo apt-get install poppler-utils
from pathlib import Path

from thumbnails_readme import thumbnails_readme

# Maximum thumbnail size - reduce to reduce final thumbnail size
max_size = (128, 128)
# PDF quality, lower the number, lower the quality
pdf_quality = 15

# Windows
poppler_path = r'C:\Program Files\poppler-0.68.0\bin'
# Linux
poppler_path = None

path = Path.cwd()
path = path.parent

# Do not forget to add your path to image thumbnails folder
skiplist = (
    '.git',
    '.github',
    '.idea',
    'idea',
    'image_thumbnails',
    '.pytest_cache',
    'thumbnails_readme',
    'venv',
    'docs',
)

path_to_thumbnails_folder = path / 'image_thumbnails'
path_to_readme = Path(path / 'README.md')

if __name__ == '__main__':
    thumbnails_readme.prepare_thumbnails_folder(path_to_thumbnails_folder)
    thumbnails_readme.prepare_readme(path_to_readme)
    thumbnails_readme.crawl(
        path,
        path_to_readme,
        path_to_thumbnails_folder,
        max_size,
        pdf_quality,
        skiplist,
        poppler_path,
    )

