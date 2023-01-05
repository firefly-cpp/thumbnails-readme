# thumbnails-readme

This is a simple library, that allows you to automatically generate thumbnails for images. It crawls through your directory and generates thumbnails for all images. It is written in Python. It uses the Pillow and pdf2image library.

Example: finds files in your directories
* ['glyph_example.pdf', 'heart-rate-monitor-to-data-mining-evolution.pdf', **'pismenka-interval.pdf'**, 'pismenka-trajanje.pdf']

Creates a thumbnails

![2023-01-05 10_54_02-000244](https://user-images.githubusercontent.com/33880044/210753771-7612a1c4-c7ec-4c75-9033-69652b816841.png)

Adds it to README.md

`![Thumbnail](/image_thumbnails/PDFpismenka-interval_thumb.png)`

![2023-01-05 11_06_43-000251](https://user-images.githubusercontent.com/33880044/210754629-b974ba51-781e-4f32-9ce9-519b57a8bfd0.png)
