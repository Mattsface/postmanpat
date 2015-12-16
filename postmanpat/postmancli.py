#!/usr/bin/env python3



from docopt import docopt
    
"""
postmanpat

Usage:
  postmanpat
  postmanpat -h | --help
  postmanpat --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  skele hello

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/rdegges/skele-cli
"""

def main():
    import commands
    options = docopt(__doc__, version=VERSION)