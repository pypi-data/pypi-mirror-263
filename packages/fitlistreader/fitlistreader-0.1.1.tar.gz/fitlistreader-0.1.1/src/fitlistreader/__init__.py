"""
fitlistreader
=============

Provides:
1. A Parser for HDTV fitlist.xml files, converting them to Sequence-like-objects
2. CLI tools to do this directly in the terminal

CLI-Utilities
-------------
 - fitlistreader : displays peak information of a given fitlist.xml file
"""
# read version from installed package
from importlib.metadata import version
from .fitlistreader import run

def run_wrapper():
    """Access for the CLI to method in non-init file."""
    run()

__version__ = version("fitlistreader")