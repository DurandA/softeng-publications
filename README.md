# softeng-publications

CLI tool to generate HTML of publications displayed on Software Engineering website

## Setup

This tools requires Python >= 3.6.

Install required packages:

```
sudo pip3 install -r requirements.txt
```

## Usage

```
usage: publications.py [-h] bibtex

positional arguments:
  bibtex

optional arguments:
  -h, --help  show this help message and exit
```

## Minimal BibTeX entry

```bibtex
@InProceedings{10.1007/978-3-319-38791-8_56,
author="Liechti, Olivier
and Pasquier, Jacques
and Pr{\'e}vost, Laurent
and Gremaud, Pascal",
title="The WoT as an Awareness Booster in Agile Development Workspaces",
booktitle="Web Engineering",
year="2016",
publisher="Springer International Publishing",
url = {https://link.springer.com/chapter/10.1007/978-3-319-38791-8_56}
}
```
