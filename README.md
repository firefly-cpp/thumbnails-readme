# thumbnails-readme --- Create thumbnails

## Create thumbnails for raster and vector images in parent and its subdirectories and append them to the README.md file

---
![PyPI Version](https://img.shields.io/pypi/v/thumbnails-readme.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/thumbnails-readme.svg)
[![Downloads](https://pepy.tech/badge/thumbnails-readme)](https://pepy.tech/project/thumbnails-readme)
![GitHub repo size](https://img.shields.io/github/repo-size/firefly-cpp/thumbnails-readme?style=flat-square)
[![GitHub license](https://img.shields.io/github/license/firefly-cpp/thumbnails-readme.svg)](https://github.com/firefly-cpp/thumbnails-readme/blob/master/LICENSE)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/firefly-cpp/thumbnails-readme.svg)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/firefly-cpp/thumbnails-readme.svg)](http://isitmaintained.com/project/firefly-cpp/thumbnails-readme "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/firefly-cpp/thumbnails-readme.svg)](http://isitmaintained.com/project/firefly-cpp/thumbnails-readme "Percentage of issues still open")

<p align="center">
  <img alt="logo" width="300" src=".github/images/logo_background.png">
</p>


## Description
The "thumbnails-readme" package is a simple library devoted to automatically generating thumbnails from a directory. It is explicitly designed to create thumbnails from Git folders and show thumbnails in the README file of that Git folder.

### Multi-pages PDFs are turned into .gif thumbnails

Current supported filetype extensions are: ".bmp", ".gif", ".ico", "jpeg", ".jpg", ".png", ".tga", ".tiff", ".webp", ".pdf" and ".svg"

## GitHub action

See also the associated GitHub action in the following repository: [thumbnails-readme-action](https://github.com/KukovecRok/thumbnails-readme-action).

## How it works?

First step: program finds graphical material in your directories
* ['fig1.pdf', 'fig2.pdf', 'fig3.pdf', 'fig4.pdf']

Second step: program generates thumbnails for each material identified in folders
![2023-01-05 10_54_06-000245](https://user-images.githubusercontent.com/33880044/212469322-e4fe49af-404d-40cd-85f8-63fd3eee162d.png)

Third step: program appends thumbnails into README

![thumbnails-readme-md-image](https://user-images.githubusercontent.com/33880044/224533101-11618c49-61b5-4b6a-bccd-5a1164430bca.png)

## Installation
Install thumbnails-readme with pip:

```sh
pip install thumbnails-readme
```

In case you want to install directly from the source code, use:

```sh
$ git clone https://github.com/firefly-cpp/thumbnails-readme.git
$ cd thumbnails-readme
$ poetry build
$ python setup.py install
```

To install thumbnails-readme on Alpine Linux, please use:

```sh
$ apk add py3-thumbnails-readme
```

To install thumbnails-readme on Arch Linux, please use an [AUR helper](https://wiki.archlinux.org/title/AUR_helpers):

```sh
$ yay -Syyu python-thumbnails-readme
```

## Additional dependencies

### Windows
Windows users have to download poppler for Windows. Add poppler
path in your Python file (see the main example).

``` poppler_path = path/to/your/poppler/bin/ ```

for example: ```poppler_path = C:/Program Files/poppler-0.68.0/bin```

### Linux
Linux's users can install poppler-utils from the main repositories.

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
thumbnails_readme.crawl(path, path_to_readme, path_to_thumbnails_folder, MAX_SIZE, pdf_quality, skiplist, poppler_path)
```
## Use Cases

[https://github.com/firefly-cpp/figures](https://github.com/firefly-cpp/figures)

[https://github.com/firefly-cpp/posters](https://github.com/firefly-cpp/posters)

## License

This package is distributed under the BSD-3-Clause license. This license can be found online at <http://www.opensource.org/licenses/bsd-3-clause/>.

## Disclaimer

This framework is provided as-is, and there are no guarantees that it fits your purposes or that it is bug-free. Use it at your own risk!

# Thumbnails
[![example-long](/image_thumbnails/pdf_animation_example-long.gif)](tests/example-long.pdf)
[![example-pdf](/image_thumbnails/pdf_example-pdf_thumb.png)](tests/example-pdf.pdf)
[![example-svg](/image_thumbnails/svg_example-svg_thumb.png)](tests/example-svg.svg)
[![arm-pipeline](/image_thumbnails/pdf_arm-pipeline_thumb.png)](tests/figures-main/association-rule-mining/arm-pipeline.pdf)
[![ARM_store](/image_thumbnails/pdf_ARM_store_thumb.png)](tests/figures-main/association-rule-mining/ARM_store.pdf)
[![ARM_store](/image_thumbnails/png_ARM_store_thumb.png)](tests/figures-main/association-rule-mining/ARM_store.png)
[![transaction-database](/image_thumbnails/pdf_transaction-database_thumb.png)](tests/figures-main/association-rule-mining/transaction-database.pdf)
[![transakcijska_baza](/image_thumbnails/pdf_transakcijska_baza_thumb.png)](tests/figures-main/association-rule-mining/transakcijska_baza.pdf)
[![automl](/image_thumbnails/pdf_automl_thumb.png)](tests/figures-main/automl/si/automl.pdf)
[![cevovod](/image_thumbnails/pdf_cevovod_thumb.png)](tests/figures-main/automl/si/cevovod.pdf)
[![niaaml](/image_thumbnails/pdf_niaaml_thumb.png)](tests/figures-main/automl/si/niaaml.pdf)
[![metrike](/image_thumbnails/pdf_metrike_thumb.png)](tests/figures-main/classification/metrike.pdf)
[![MnozicaUcnaValidacijskaTestna](/image_thumbnails/pdf_MnozicaUcnaValidacijskaTestna_thumb.png)](tests/figures-main/classification/MnozicaUcnaValidacijskaTestna.pdf)
[![PodatkovnaUcnaValidacijskaTestnaMnozica](/image_thumbnails/pdf_PodatkovnaUcnaValidacijskaTestnaMnozica_thumb.png)](tests/figures-main/classification/PodatkovnaUcnaValidacijskaTestnaMnozica.pdf)
[![podrocja-strojnega-ucenja](/image_thumbnails/pdf_podrocja-strojnega-ucenja_thumb.png)](tests/figures-main/classification/podrocja-strojnega-ucenja.pdf)
[![podrocja-strojnega-ucenja](/image_thumbnails/png_podrocja-strojnega-ucenja_thumb.png)](tests/figures-main/classification/podrocja-strojnega-ucenja.png)
[![VariancaPristranskost](/image_thumbnails/pdf_VariancaPristranskost_thumb.png)](tests/figures-main/classification/VariancaPristranskost.pdf)
[![primer-grucenje-sport](/image_thumbnails/pdf_primer-grucenje-sport_thumb.png)](tests/figures-main/clustering/primer-grucenje-sport.pdf)
[![Ciscenje_podatkov](/image_thumbnails/pdf_Ciscenje_podatkov_thumb.png)](tests/figures-main/data-cleaning/Ciscenje_podatkov.pdf)
[![Ciscenje_podatkov](/image_thumbnails/png_Ciscenje_podatkov_thumb.png)](tests/figures-main/data-cleaning/Ciscenje_podatkov.png)
[![rudar](/image_thumbnails/png_rudar_thumb.png)](tests/figures-main/data-mining/rudar.png)
[![Atributte_Instance](/image_thumbnails/pdf_Atributte_Instance_thumb.png)](tests/figures-main/data-mining/DM_steps/Atributte_Instance.pdf)
[![Atributte_Instance](/image_thumbnails/png_Atributte_Instance_thumb.png)](tests/figures-main/data-mining/DM_steps/Atributte_Instance.png)
[![Atributte_Instance_missing_data](/image_thumbnails/pdf_Atributte_Instance_missing_data_thumb.png)](tests/figures-main/data-mining/DM_steps/Atributte_Instance_missing_data.pdf)
[![Atribut_Instanca](/image_thumbnails/pdf_Atribut_Instanca_thumb.png)](tests/figures-main/data-mining/DM_steps/Atribut_Instanca.pdf)
[![Atribut_Instanca](/image_thumbnails/png_Atribut_Instanca_thumb.png)](tests/figures-main/data-mining/DM_steps/Atribut_Instanca.png)
[![Atribut_Instanca_missing_data](/image_thumbnails/pdf_Atribut_Instanca_missing_data_thumb.png)](tests/figures-main/data-mining/DM_steps/Atribut_Instanca_missing_data.pdf)
[![Atribut_Instanca_missing_data](/image_thumbnails/png_Atribut_Instanca_missing_data_thumb.png)](tests/figures-main/data-mining/DM_steps/Atribut_Instanca_missing_data.png)
[![Atrribut_Instance_missing_data](/image_thumbnails/png_Atrribut_Instance_missing_data_thumb.png)](tests/figures-main/data-mining/DM_steps/Atrribut_Instance_missing_data.png)
[![DM_steps](/image_thumbnails/pdf_DM_steps_thumb.png)](tests/figures-main/data-mining/DM_steps/DM_steps.pdf)
[![DM_steps](/image_thumbnails/png_DM_steps_thumb.png)](tests/figures-main/data-mining/DM_steps/DM_steps.png)
[![DM_steps_slo](/image_thumbnails/pdf_DM_steps_slo_thumb.png)](tests/figures-main/data-mining/DM_steps/DM_steps_slo.pdf)
[![DM_steps_slo](/image_thumbnails/png_DM_steps_slo_thumb.png)](tests/figures-main/data-mining/DM_steps/DM_steps_slo.png)
[![one-hot-encoding](/image_thumbnails/pdf_one-hot-encoding_thumb.png)](tests/figures-main/data-mining/preprocessing/one-hot-encoding.pdf)
[![ordinal-encoding](/image_thumbnails/pdf_ordinal-encoding_thumb.png)](tests/figures-main/data-mining/preprocessing/ordinal-encoding.pdf)
[![Vrstice_stolpci](/image_thumbnails/pdf_Vrstice_stolpci_thumb.png)](tests/figures-main/data-mining/preprocessing/Vrstice_stolpci.pdf)
[![Vrstice_stolpci](/image_thumbnails/png_Vrstice_stolpci_thumb.png)](tests/figures-main/data-mining/preprocessing/Vrstice_stolpci.png)
[![glyph_example](/image_thumbnails/pdf_glyph_example_thumb.png)](tests/figures-main/data-mining-in-sport/glyph_example.pdf)
[![heart-rate-monitor-to-data-mining-evolution](/image_thumbnails/pdf_heart-rate-monitor-to-data-mining-evolution_thumb.png)](tests/figures-main/data-mining-in-sport/heart-rate-monitor-to-data-mining-evolution.pdf)
[![pismenka-interval](/image_thumbnails/pdf_pismenka-interval_thumb.png)](tests/figures-main/data-mining-in-sport/pismenka-interval.pdf)
[![pismenka-trajanje](/image_thumbnails/pdf_pismenka-trajanje_thumb.png)](tests/figures-main/data-mining-in-sport/pismenka-trajanje.pdf)
[![ast-diagram-1](/image_thumbnails/pdf_ast-diagram-1_thumb.png)](tests/figures-main/digital-twin/artificial-sport-trainer/ast-diagram-1.pdf)
[![ast-monitor](/image_thumbnails/jpg_ast-monitor_thumb.png)](tests/figures-main/digital-twin/artificial-sport-trainer/ast-monitor.JPG)
[![ast-outline-1](/image_thumbnails/pdf_ast-outline-1_thumb.png)](tests/figures-main/digital-twin/artificial-sport-trainer/ast-outline-1.pdf)
[![digital-twin-model](/image_thumbnails/png_digital-twin-model_thumb.png)](tests/figures-main/digital-twin/model-EN/digital-twin-model.png)
[![digital-twin-model](/image_thumbnails/svg_digital-twin-model_thumb.png)](tests/figures-main/digital-twin/model-EN/digital-twin-model.svg)
[![digital-twin-model](/image_thumbnails/png_digital-twin-model_thumb.png)](tests/figures-main/digital-twin/model-SI/digital-twin-model.png)
[![digital-twin-model](/image_thumbnails/svg_digital-twin-model_thumb.png)](tests/figures-main/digital-twin/model-SI/digital-twin-model.svg)
[![feature-selection](/image_thumbnails/pdf_feature-selection_thumb.png)](tests/figures-main/feature-selection/feature-selection.pdf)
[![izbira-znacilnic](/image_thumbnails/pdf_izbira-znacilnic_thumb.png)](tests/figures-main/feature-selection/izbira-znacilnic.pdf)
[![jumper-wires](/image_thumbnails/jpg_jumper-wires_thumb.png)](tests/figures-main/hardware/jumper-wires.JPG)
[![smart_watch_and_ant+](/image_thumbnails/jpg_smart_watch_and_ant+_thumb.png)](tests/figures-main/hardware/smart_watch_and_ant+.jpg)
[![ants](/image_thumbnails/pdf_ants_thumb.png)](tests/figures-main/nature-inspired-algorithms/ants.pdf)
[![mapping](/image_thumbnails/pdf_mapping_thumb.png)](tests/figures-main/nature-inspired-algorithms/mapping.pdf)
[![natural_evolution_bears](/image_thumbnails/pdf_natural_evolution_bears_thumb.png)](tests/figures-main/nature-inspired-algorithms/natural_evolution_bears.pdf)
[![natural_evolution_bears](/image_thumbnails/png_natural_evolution_bears_thumb.png)](tests/figures-main/nature-inspired-algorithms/natural_evolution_bears.png)
[![natural_evolution_bears_small](/image_thumbnails/png_natural_evolution_bears_small_thumb.png)](tests/figures-main/nature-inspired-algorithms/natural_evolution_bears_small.png)
[![ring4](/image_thumbnails/pdf_ring4_thumb.png)](tests/figures-main/nature-inspired-algorithms/ring4.pdf)
[![nevronska-mreza-primer](/image_thumbnails/pdf_nevronska-mreza-primer_thumb.png)](tests/figures-main/neural-network/nevronska-mreza-primer.pdf)
[![NiaLogos](/image_thumbnails/png_NiaLogos_thumb.png)](tests/figures-main/nialogos/NiaLogos.png)
[![BSD](/image_thumbnails/pdf_BSD_thumb.png)](tests/figures-main/other/BSD.pdf)
[![BSD](/image_thumbnails/svg_BSD_thumb.png)](tests/figures-main/other/BSD.svg)
[![BSD_attribution](/image_thumbnails/pdf_BSD_attribution_thumb.png)](tests/figures-main/other/BSD_attribution.pdf)
[![BSD_no_attribution](/image_thumbnails/pdf_BSD_no_attribution_thumb.png)](tests/figures-main/other/BSD_no_attribution.pdf)
[![hvala](/image_thumbnails/pdf_hvala_thumb.png)](tests/figures-main/other/hvala.pdf)
[![LinuxDistro](/image_thumbnails/pdf_LinuxDistro_thumb.png)](tests/figures-main/other/LinuxDistro.pdf)
[![LinuxDistro_attribution](/image_thumbnails/pdf_LinuxDistro_attribution_thumb.png)](tests/figures-main/other/LinuxDistro_attribution.pdf)
[![niapy_logo](/image_thumbnails/png_niapy_logo_thumb.png)](tests/figures-main/other/niapy_logo.png)
[![OS](/image_thumbnails/pdf_OS_thumb.png)](tests/figures-main/other/OS.pdf)
[![OS_no_attribution](/image_thumbnails/pdf_OS_no_attribution_thumb.png)](tests/figures-main/other/OS_no_attribution.pdf)
[![PortaliInSistemiZnanja_logotipi](/image_thumbnails/pdf_PortaliInSistemiZnanja_logotipi_thumb.png)](tests/figures-main/other/PortaliInSistemiZnanja_logotipi.pdf)
[![PortaliInSistemiZnanja_logotipi_no_attribution](/image_thumbnails/pdf_PortaliInSistemiZnanja_logotipi_no_attribution_thumb.png)](tests/figures-main/other/PortaliInSistemiZnanja_logotipi_no_attribution.pdf)
[![vprasaj](/image_thumbnails/pdf_vprasaj_thumb.png)](tests/figures-main/other/vprasaj.pdf)
[![gradniki](/image_thumbnails/png_gradniki_thumb.png)](tests/figures-main/programming/haskell/yesod-framework/gradniki.PNG)
[![hello_world](/image_thumbnails/png_hello_world_thumb.png)](tests/figures-main/programming/haskell/yesod-framework/hello_world.PNG)
[![hello_yesod](/image_thumbnails/png_hello_yesod_thumb.png)](tests/figures-main/programming/haskell/yesod-framework/hello_yesod.PNG)
[![popularnost-haskell](/image_thumbnails/png_popularnost-haskell_thumb.png)](tests/figures-main/programming/haskell/yesod-framework/popularnost-haskell.PNG)
[![sport-activities-features](/image_thumbnails/pdf_sport-activities-features_thumb.png)](tests/figures-main/software-packages/sport-activities-features.pdf)
