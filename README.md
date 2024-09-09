<p align="center">
  <img alt="logo" width="300" src=".github/images/logo_background.png">
</p>

<h1 align="center">
  thumbnails-readme
</h1>

<h2 align="center">
  Create thumbnails for raster and vector images in parent and its subdirectories and append them to the README.md file
</h2>

<p align="center">
  <img alt="PyPI Version" src="https://img.shields.io/pypi/v/thumbnails-readme.svg">
  <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/thumbnails-readme.svg">
  <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/thumbnails-readme.svg">
  <a href="https://repology.org/project/python:thumbnails-readme/versions">
    <img alt="Packaging status" src="https://repology.org/badge/tiny-repos/python:thumbnails-readme.svg">
  </a>
  <a href="https://pepy.tech/project/thumbnails-readme">
    <img alt="Downloads" src="https://pepy.tech/badge/thumbnails-readme">
  </a>
  <a href="https://github.com/firefly-cpp/thumbnails-readme/blob/master/LICENSE">
    <img alt="GitHub License" src="https://img.shields.io/github/license/firefly-cpp/thumbnails-readme.svg">
  </a>
</p>

<p align="center">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/firefly-cpp/thumbnails-readme">
  <img alt="GitHub Commit Activity" src="https://img.shields.io/github/commit-activity/w/firefly-cpp/thumbnails-readme.svg">
  <a href='http://isitmaintained.com/project/firefly-cpp/thumbnails-readme "Average time to resolve an issue"'>
    <img alt="Average time to resolve an issue" src="http://isitmaintained.com/badge/resolution/firefly-cpp/thumbnails-readme.svg">
  </a>
  <a href='http://isitmaintained.com/project/firefly-cpp/thumbnails-readme "Percentage of issues still open"'>
    <img alt="Percentage of issues still open" src="http://isitmaintained.com/badge/open/firefly-cpp/thumbnails-readme.svg">
  </a>
</p>

<p align="center">
  <a href="#-github-action">🚀 GitHub Action</a> •
  <a href="#-how-does-it-work">💡 How does it work?</a> •
  <a href="#-installation">📦 Installation</a> •
  <a href="#-additional-dependencies">🔗 Additional dependencies</a> •
  <a href="#-example">📓 Example</a> •
  <a href="#-use-cases">📂 Use Cases</a> •
  <a href="#-license">🔑 License</a> •
  <a href="#-thumbnails">📷 Thumbnails</a>
</p>

The `thumbnails-readme` package is a simple library devoted to automatically generating thumbnails from a directory. It is explicitly designed to create thumbnails from Git folders. The thumbnails are shown in the README file of that Git folder. 📁🌐📸

### 🔄 Multi-page PDFs are turned into .gif thumbnails

Current supported filetype extensions are: `.bmp`, `.gif`, `.ico`, `jpeg`, `.jpg`, `.png`, `.tga`, `.tiff`, `.webp`, `.pdf`, and `.svg`

## 🚀 GitHub Action

See the associated GitHub Action in the following repository: [thumbnails-readme-action](https://github.com/KukovecRok/thumbnails-readme-action).

## 💡 How does it work?

In the first step the program finds graphical material in your directories:
* ['fig1.pdf', 'fig2.pdf', 'fig3.pdf', 'fig4.pdf']

In the second step the program generates thumbnails for each material identified in folders.

![2023-01-05 10_54_06-000245](https://user-images.githubusercontent.com/33880044/212469322-e4fe49af-404d-40cd-85f8-63fd3eee162d.png)

In the third step the program appends thumbnails to the README file.

![thumbnails-readme-md-image](https://user-images.githubusercontent.com/33880044/224533101-11618c49-61b5-4b6a-bccd-5a1164430bca.png)

## 📦 Installation

To install `thumbnails-readme` with pip, use:

```sh
pip install thumbnails-readme
```

To install `thumbnails-readme` directly from the source code, use:

```sh
$ git clone https://github.com/firefly-cpp/thumbnails-readme.git
$ cd thumbnails-readme
$ poetry build
$ python setup.py install
```

To install `thumbnails-readme` on Alpine Linux, please use:

```sh
$ apk add py3-thumbnails-readme
```

To install `thumbnails-readme` on Arch Linux, use an [AUR helper](https://wiki.archlinux.org/title/AUR_helpers):

```sh
$ yay -Syyu python-thumbnails-readme
```

## 🔗 Additional dependencies

### Windows
Windows users have to download poppler for Windows. Add poppler path in your Python file (see the main example).

``` poppler_path = path/to/your/poppler/bin/ ```

For example: ```poppler_path = C:/Program Files/poppler-0.68.0/bin```

### Linux
Linux's users can install poppler-utils from the main repositories.

## 📓 Examples

### Examples of Usage

```python
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

### Run the script

``` python
# Prepare thumbnails folder (check if exists, delete old thumbnails and create new ones)
thumbnails_readme.prepare_thumbnails_folder(path_to_thumbnails_folder)

# Prepare README.md file (check if exists, delete last modifications and place newly generated ones)
thumbnails_readme.prepare_readme(path_to_readme)

# Generate thumbnails
thumbnails_readme.crawl(path, path_to_readme, path_to_thumbnails_folder, MAX_SIZE, pdf_quality, skiplist, poppler_path)
```
## 📂 Use Cases

- [https://github.com/firefly-cpp/figures](https://github.com/firefly-cpp/figures)
- [https://github.com/firefly-cpp/posters](https://github.com/firefly-cpp/posters)

## 🔑 License

This package is distributed under the BSD-3-Clause license. This license can be found online at <http://www.opensource.org/licenses/bsd-3-clause/>.

## Disclaimer

This framework is provided as-is, and there are no guarantees that it fits your purposes or that it is bug-free. Use it at your own risk!

## 📷 Thumbnails

[![example-long](/image_thumbnails/pdf_animation_example-long.gif)](tests/example-long.pdf)
[![example-pdf](/image_thumbnails/pdf_example-pdf_thumb.png)](tests/example-pdf.pdf)
[![example-svg](/image_thumbnails/svg_example-svg_thumb.png)](tests/example-svg.svg)
