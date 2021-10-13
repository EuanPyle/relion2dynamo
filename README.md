# Relion2Dynamo
## Converts Star Files from RELION 4.0 to Dynamo Table with Metadata for Motl File Generation

[![PyPI pyversions](https://img.shields.io/pypi/pyversions/dynamo2m.svg)](https://pypi.python.org/pypi/dynamo2m/)

Based on [dynamo2m](df1) by Alister Burt.

## Installation

Installation is carried out via:
```sh
pip install relion2dynamo
```

## Requirements

Input must be a star file with a data_particles field, e.g. run_data.star from Refine3D or any _data.star

## Usage

Invoke from the command line via typing:
```sh
relion2dynamo
```
and input:
```sh
Input Star File: example.star
Output Tbl file: test.tbl
```
