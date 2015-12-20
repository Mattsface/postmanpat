#!/usr/bin/env python3



from docopt import docopt

"""
postmanpat

Usage:
  postmancli delete
  postmancli move
  postmancli read
  postmancl
  postmancli -h | --help
  postmancli --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  postmancli delete

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/rdegges/skele-cli
"""

def main():
    import commands
    options = docopt(__doc__, version=VERSION)

    print(options)

def read_config():
    pass