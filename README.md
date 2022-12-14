# Relion2Dynamo
## Converts Star Files from RELION 4.0 to Dynamo Table

Based on [dynamo2m](https://github.com/alisterburt/dynamo2m) by Alister Burt.

## Installation

Installation is carried out via:
```sh
pip install relion2dynamo
```

## Requirements

Your tomogram names (rlnTomoName) must be some variant of:

```sh
[any_string]_[number which refers to tomogram number]
e.g. TS_01 or ts_1 or tomogram_10
```

## Usage

Invoke from the command line and specify input star file and, optionally, the desired output table file name
```sh
relion2dynamo --relion-star-file [name] --dynamo-table-file [name]
```
