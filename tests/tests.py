#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from builtins import str
import unittest
import importlib
import hashlib
import traceback
import sys
import os
import datetime
from ddt import ddt, data, unpack
# added parent path so we can import shelterparser module
sys.path.insert(0, os.path.abspath('..'))

from shelterparser.importers import ShelterImporter, SHELTERS
from shelterparser import utils

# ID of shelter, when we want to limit tests to only one shelter
SHELTER_ID = None

_counter = 0


class StopShelterTestGeneration(Exception):
    pass


def _get_counter():
    global _counter
    _counter += 1
    return _counter


class ShelterImporterTester(ShelterImporter):

    def __init__(self, url, folder):
        super(ShelterImporterTester, self).__init__(url)
        self.folder = folder

        self.data = importlib.import_module("test_data.%s.%s.data" % (utils.name_from_url(url), utils.name_from_url_rest(url)))
        print("Imported data: %s" % self.data)

    def _iter_detail_urls(self):
        detail_urls = []
        try:
            for url in super(ShelterImporterTester, self)._iter_detail_urls(first_page_only=True):
                print("Detail URL: %s" % url)
                detail_urls.append(url)
        except StopIteration:
            pass

        setattr(ListParserTest, "pokus_test", test_generator_equal(1, 1))

        print("Testing detail URLs...%s" % detail_urls)
        for url, _ in self.data.URL_REWRITES[1:]:
            print("Testing detail URL presence: %s" % url)
            test_name = 'test_detail_url_%s_%d' % (utils.name_from_url(self.url), _get_counter())
            test = test_generator_true(url in detail_urls)
            setattr(ListParserTest, test_name, test)

        for url in detail_urls:
            yield str(url)

    def _get_data_from_url(self, url):
        print("Trying rewrite URL %s..." % url)
        if url in dict(self.data.URL_REWRITES):
            url = dict(self.data.URL_REWRITES)[url]
            print("Url rewrited to '%s'" % url)
        else:
            raise StopShelterTestGeneration()
        data = super(ShelterImporterTester, self)._get_data_from_url(url)
        return data

    def _get_animal(self, url):
        animal = super(ShelterImporterTester, self)._get_animal(url)
        print("Testing animal data...")

        for key, test_value in list(self.data.ANIMALS[url].items()):

            animal_data = animal.get_dict()
            val = animal_data[key] if key in animal_data else None

            test_name = 'test_animal_%s_%s_%s_%d' % (utils.name_from_url(self.url), utils.name_from_url_rest(self.url), key, _get_counter())
            test = test_generator_equal(test_value, val)
            # print "Adding test '%s'%s: %s" % (test_name, key, test_value)
            setattr(DetailParserTest, test_name, test)
        return animal

    def __generate_hash(self, url):
        h = hashlib.md5(url)
        return h.hexdigest()


@ddt
class DetailParserTest(unittest.TestCase):

    @data(
        (u"2011", datetime.date(2011, 1, 1)),
        (u"1980 Leden", datetime.date(1980, 1, 1)),
        (u"únor 2013", datetime.date(2013, 2, 1)),
        (u"Březen 2014", datetime.date(2014, 3, 1)),
        (u"duben 2014", datetime.date(2014, 4, 1)),
        (u"květen 2014", datetime.date(2014, 5, 1)),
        (u"červen 2014", datetime.date(2014, 6, 1)),
        (u"červenec 2014", datetime.date(2014, 7, 1)),
        (u"srpen 2014", datetime.date(2014, 8, 1)),
        (u"září 2014", datetime.date(2014, 9, 1)),
        (u"říjen 2014", datetime.date(2014, 10, 1)),
        (u"listopad 2014", datetime.date(2014, 11, 1)),
        (u"prosinec 2014", datetime.date(2014, 12, 1)),
        (u"11/2012", datetime.date(2012, 11, 1)),
        (u"23.2.1999", datetime.date(1999, 2, 23)),
        (u"01.02.2003", datetime.date(2003, 2, 1)),
        (u"15/11/2014", datetime.date(2014, 11, 15)),
        (u"F-M 2.2.2014", datetime.date(2014, 2, 2)),
    )
    @unpack
    def test_utils_parser_date(self, orig, expected):
        self.assertEqual(utils.parse_date(orig), expected)


class ListParserTest(unittest.TestCase):
    pass


def test_generator_equal(a, b):
    def test(self):
        self.assertEqual(a, b)
    return test


def test_generator_true(a):
    def test(self):
        self.assertTrue(a)
    return test


def generate_tests():
    print("==Setting up...")
    for shelter in SHELTERS:

        if SHELTER_ID is not None and shelter['shelter_id'] != SHELTER_ID:
            continue

        for import_url in shelter['urls']:
            try:
                importer = ShelterImporterTester(import_url, utils.name_from_url(import_url))
                print(importer)

                for animal in importer.iter_animals():
                    pass
                    # print "----Animal: %s" % animal
            except ImportError:
                print("====== SKIPPING %s - no test data! ======" % import_url)
            except StopShelterTestGeneration:
                print("Stopping test generation for %s." % import_url)
            except Exception as e:
                print("Error: %s" % e)
                print(traceback.format_exc())
                exit(1)


def suite():
    suite = unittest.TestSuite()
    generate_tests()
    suite.addTest(unittest.makeSuite(ListParserTest))
    suite.addTest(unittest.makeSuite(DetailParserTest))
    return suite

if __name__ == '__main__':

    # you can limit tests to only one shelter by adding a parameter with shelter ID
    if len(sys.argv) > 1:
        SHELTER_ID = int(sys.argv[1])
        print("Set shelter_id to %d" % SHELTER_ID)
        del sys.argv[1:]

    unittest.main(defaultTest='suite')

