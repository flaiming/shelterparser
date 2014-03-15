# -*- coding: utf-8 -*-
import os
import urllib2
import tarfile
import tempfile
from bs4 import BeautifulSoup


class Opener(object):

    def __init__(self, path, encoding=""):
        self.path = path
        self.encoding = encoding
        self.content_type = ""

    def get_encoding(self):
        return self.encoding

    def get_content_type(self):
        return self.content_type

    def _universal_opener(self):
        data = ""
        if self.path.startswith('http'):
            response = urllib2.urlopen(self.path)
            self.content_type = response.info().gettype()
            print "Content type of '%s': '%s'" % (self.path, self.content_type)
            data = response.read()
            try:
                response.close()
            except:
                pass
        else:
            with open(self.path) as f:
                data = f.read()
        return data

    def _decode(self, data):
        if not self.encoding:
            soup = BeautifulSoup(data)
            if hasattr(soup, 'original_encoding') and soup.original_encoding:
                self.encoding = soup.original_encoding
        if self.encoding:
            print "Decoding data from '%s' to unicode." % self.encoding
            data = data.decode(self.encoding, 'replace')
        return data

    def read(self):
        """
        Reads the data from given source.
        Raises urllib2.HTTPError, urllib2.URLError (subclasses of IOError) or IOError if problem encountered.
        """
        data = self._universal_opener()
        data = self._decode(data)
        return data

    def __str__(self):
        return "Opener with path '%s', encoding '%s'" % (self.path, self.encoding)

