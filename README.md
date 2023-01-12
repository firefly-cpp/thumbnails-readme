# thumbnails-readme --- Create thumbnails

---
![PyPI Version](https://img.shields.io/pypi/v/thumbnails-readme.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/thumbnails-readme.svg)
[![Downloads](https://pepy.tech/badge/thumbnails-readme)](https://pepy.tech/project/thumbnails-readme)
[![GitHub license](https://img.shields.io/github/license/firefly-cpp/thumbnails-readme.svg)](https://github.com/firefly-cpp/thumbnails-readme/blob/master/LICENSE)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/firefly-cpp/thumbnails-readme.svg)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/firefly-cpp/thumbnails-readme.svg)](http://isitmaintained.com/project/firefly-cpp/thumbnails-readme "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/firefly-cpp/thumbnails-readme.svg)](http://isitmaintained.com/project/firefly-cpp/thumbnails-readme "Percentage of issues still open")

## Description
The "thumbnails-readme" package is a simple library devoted to automatically generating thumbnails from a directory. It is explicitly designed to create thumbnails from Git folders and show thumbnails in the README file of that Git folder.

## How it works?

First step: program finds graphical material in your directories
* ['fig1.pdf', 'fig2.pdf', 'fig3.pdf', 'fig4.pdf']

Second step: program generates thumbnails for each material identified in folders
![2023-01-05 10_54_02-000244](https://user-images.githubusercontent.com/33880044/210753771-7612a1c4-c7ec-4c75-9033-69652b816841.png)

Third step: program appends thumbnails into README
`![Thumbnail](/image_thumbnails/PDFpismenka-interval_thumb.png)`

![2023-01-05 11_06_43-000251](https://user-images.githubusercontent.com/33880044/210754629-b974ba51-781e-4f32-9ce9-519b57a8bfd0.png)

## Installation

```sh
pip install thumbnails-readme
```

## Additional dependencies

### Windows
Windows users have to download poppler for Windows. Add poppler
path in your Python file (see the main example).

``` poppler_path = path/to/your/poppler/bin/ ```

for example: ```poppler_path = C:/Program Files/poppler-0.68.0/bin```

### Linux
Linux users can install poppler-utils from the main repositories.

### Example

``` python
# Maximum thumbnail size - lower the number, smaller the thumbnail
MAX_SIZE = (128, 128)

# PDF quality, lower the number, lower the quality
pdf_quality = 15

# Skiplist - which directories to ignore
skiplist = (
    ".git",
    )


# Path to your directory
path = os.getcwd()
path = os.path.dirname(path)

# Path to the folder, you want new thumbnails to be placed in
path_to_thumbnails_folder = Path(path + "/image_thumbnails")

# Path to README.md file to be written to
path_to_readme = Path(path + "/README.md")
```

## Run the script

``` python
# Prepare thumbnails folder (check if exists, delete old thumbnails and create new ones)
thumbnails_readme.prepare_thumbnails_folder(path_to_thumbnails_folder)

# Prepare README.md file (check if exists, delete last modifications and place newly generated ones)
thumbnails_readme.prepare_readme(path_to_readme)

# Generate thumbnails
thumbnails_readme.generate_thumbnails(path, path_to_thumbnails_folder, path_to_readme, MAX_SIZE, pdf_quality, skiplist)
```

## License

This package is distributed under the MIT License. This license can be found online at <http://www.opensource.org/licenses/MIT>.

## Disclaimer

This framework is provided as-is, and there are no guarantees that it fits your purposes or that it is bug-free. Use it at your own risk!
