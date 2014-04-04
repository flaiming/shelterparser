#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import traceback
import pprint
# added parent path so we can import shelterparser module
sys.path.append(os.path.abspath('..'))

from shelterparser.parsers import HtmlParser
from shelterparser.openers import Opener


def main():
    path = ""
    domain = "http://www.fakeurl.com"
    if len(sys.argv) >= 2:
        path = sys.argv[1]
        if len(sys.argv) == 3:
            domain = sys.argv[2]
    else:
        print """
        Parse animal list from URL or file.

        $ parse_list.py <url|file> [<url>]
        """
        return False
    print "Processing '%s'..." % (path)
    try:

        opener = Opener(path)
        parser = HtmlParser(opener.read(), domain)
        for url in parser.get_urls():
            pprint.pprint(url)

    except IOError as e:
        print "Cannot open path %s: %s" % (path, e.strerror)
        traceback.print_exc()
        exit(1)


if __name__ == '__main__':
    main()

