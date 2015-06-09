#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import os
import traceback
import pprint
# added parent path so we can import shelterparser module
sys.path.append(os.path.abspath('..'))

from shelterparser.parsers import DetailParser
from shelterparser.openers import Opener
from shelterparser import utils


def main():
    path = ""
    if len(sys.argv) >= 2:
        path = sys.argv[1]
    else:
        print("""
        Parse animal detail from URL or file.

        $ parse_detail.py <url|file>
        """)
        return False
    print("Processing '%s'..." % (path))
    try:

        base_url = utils.get_base_url(path)
        if base_url == path:
            base_url = "http://fakeurl.com"

        opener = Opener(path)
        detail = DetailParser(opener.read(), base_url)
        animal = detail.get_animal()
        pprint.pprint(animal.get_dict())

    except IOError as e:
        print("Cannot open path %s: %s" % (path, e.strerror))
        traceback.print_exc()
        exit(1)


if __name__ == '__main__':
    main()

