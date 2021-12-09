# Relion2Dynamo
## Converts Star Files from RELION 4.0 to Dynamo Table with Metadata for Motl File Generation

[![PyPI pyversions](https://img.shields.io/pypi/pyversions/dynamo2m.svg)](https://pypi.python.org/pypi/dynamo2m/)

Based on [dynamo2m](https://github.com/alisterburt/dynamo2m) by Alister Burt.

## Installation

Installation is carried out via:
```sh
pip install relion2dynamo
```

## Requirements

Input must be a star file with a data_particles field, e.g. run_data.star from Refine3D or any _data.star.

Your tomogram names (rlnTomoName) must be some variant of:

```sh
[any_string]_[number which refers to tomogram number]
e.g. TS_01 or ts_1 or tomogram_10
```

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

Generate motl files via loading Matlab, Dynamo, and running the dynamotable2motl.m script packaged in the main directory to generate motl files:

```sh
Input Tbl File: test.tbl
Output Directory file: ./motl/ #Generate a new directory called motl/
```
