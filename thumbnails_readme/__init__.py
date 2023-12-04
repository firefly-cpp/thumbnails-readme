"""Init file for thumbnails_readme package."""

from thumbnails_readme.thumbnails_readme import (
    ImageThumbnail,
    crawl,
    prepare_readme,
    prepare_thumbnails_folder,
)

__all__ = [
    'ImageThumbnail',
    'crawl',
    'prepare_readme',
    'prepare_thumbnails_folder',
]

__version__ = '0.4.1'
__project__ = 'thumbnails_readme'
