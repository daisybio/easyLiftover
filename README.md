# easy-liftover

This repository wraps the [pyliftover](https://pypi.org/project/pyliftover/) package to provide an option for lifting over common file types.

## Installation
### PyPi
This package is available via [PyPi](https://pypi.org/project/easyliftover/). To install it, run:
```
pip install easyliftover
```
### Docker
This package is also available as a [Docker image](https://hub.docker.com/r/bigdatainbiomedicine/easyliftover). To use it, run:
```
docker pull bigdatainbiomedicine/easyliftover
```

## Usage
```python
from easyliftover import liftover_path, liftover_url

result = liftover_path(<fromGenome>, <toGenome>, <path>, <fileType>)
result = liftover_url(<fromGenome>, <toGenome>, <url>, <fileType>)
```
The fileType parameter is optional. If it is not provided, the file type will be inferred from the file extension.

## Supported file types
Information about which file types are supported can be found [here](https://github.com/biomedbigdata/easyLiftover/blob/main/easyliftover/types.json)