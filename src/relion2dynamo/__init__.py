"""Converts RELION particle star files to Dynamo tables."""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("relion2dynamo")
except PackageNotFoundError:
    __version__ = "uninstalled"

__author__ = "Euan Pyle"
__email__ = "euanpyle@gmail.com"
