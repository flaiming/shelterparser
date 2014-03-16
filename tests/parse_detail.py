#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import traceback
import pprint
# added parent path so we can import shelterparser module
sys.path.append(os.path.abspath('..'))

from shelterparser.parsers import DetailParser
from shelterparser.openers import Opener


def main():
    path = ""
    if len(sys.argv) >= 2:
        path = sys.argv[1]
    else:
        print """
        Parse animal detail from URL or file.

        $ parse_detail.py <url|file>
        """
        return False
    print "Processing '%s'..." % (path)
    try:

        opener = Opener(path)
        detail = DetailParser(opener.read(), 'http://www.fakeurl.com')
        pprint.pprint(detail.get_animal().get_dict())

    except IOError as e:
        print "Cannot open path %s: %s" % (path, e.strerror)
        traceback.print_exc()
        exit(1)


if __name__ == '__main__':
    main()

