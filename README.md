# LaDictionary

## Table of Contents
* [About](#about)
* [Technologies](#technologies)
* [Installation](#installation)
* [Usage](#usage)

## About
LaDictionary, or LaDic for short, provides a simple, cross-platform GUI interface for adding vocabulary words to your personal dictionary, created in LaTeX.

## Technologies
This project uses
* Python 3.8
* [MiKTeX 2.9](https://miktex.org/howto/download-miktex-2-9) (Windows)
* TeX Live 2021 (Linux)
* BeautifulSoup 4.9
* PyQt 6.1

## Installation

### Windows:
You can find a .msi installer over at [https://davidmniu.github.io/LaDictionary/](https://davidmniu.github.io/LaDictionary/). Otherwise, you can either run this program via Python itself or create the installer manually. To run with Python, simply clone this repository, open Command Prompt, `cd` into the directory and enter

```
pip install -r requirements.txt
python main.py
```

If you want to create the installer manually, `cd` into the root directory of the project and enter

```
pip install -r requirements.txt
python setup.py bdist_msi
```
upon which you should have a .msi executable installer in the /dist/ directory.

### Linux:
Support for an installer is coming soon! In the meantime, simply clone and `cd` into the repository, then run

```
pip install -r requirements.txt && python main.py
```

## Usage
The functionality of LaDic is quite straightforward; simply enter a word in the search bar, cut down the pronunciation as necessary, select your desired definitions, and press 'Save'. As of the current version, you may only select definitions of a single lexical category, these being nouns, verbs, adjectives, etc.

### LaTeX Packages
Depending on your LaTeX distribution, you may or may not have all the necessary `.sty` files already included on your first time running LaDic. If you are using MiKTeX with "Install missing packages on the fly" enabled, you can open LaDic, then search a word and press 'Save', upon which MiKTeX will install your required `.sty` files. Otherwise, you can install them manually using [MiKTeX Console](https://tex.stackexchange.com/questions/484084/how-can-i-install-a-package-on-miktex); besides a base MiKTeX install, you will need

* geometry
* palatino
* microtype
* titlesec
* fancyhdr

If you are on Linux using TeX Live, you probably know how to get these packages installed.
