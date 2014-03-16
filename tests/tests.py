#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import importlib
import hashlib
import traceback
import sys
import os
# added parent path so we can import shelterparser module
sys.path.insert(0, os.path.abspath('..'))

from shelterparser.importers import ShelterImporter, SHELTERS
from shelterparser import utils

# ID of shelter, when we want to limit tests to only one shelter
SHELTER_ID = None

TEST_MAX_ANIMALS = 5


class ShelterImporterTester(ShelterImporter):

    def __init__(self, url, folder):
        super(ShelterImporterTester, self).__init__(url)
        self.folder = folder
        self.counter = 0

        self.data = importlib.import_module("test_data.%s.%s.data" % (utils.name_from_url(url), utils.name_from_url_rest(url)))
        print "Imported data: %s" % self.data

    def __get_hash(self, url=""):
        self.counter += 1
        return hashlib.md5(str(self.counter) + url).hexdigest()

    def _get_detail_urls(self):
        detail_urls = super(ShelterImporterTester, self)._get_detail_urls()

        print "Testing detail URLs..."
        counter = 0
        for url in detail_urls:
            print "Testing detail URL %s" % url
            test_name = 'test_detail_url_%s_%s' % (utils.name_from_url(self.url), self.__get_hash())
            test = test_generator_equal(url, self.data.URL_REWRITES[counter + 1][0])
            setattr(ListParserTest, test_name, test)
            counter += 1
            if counter >= TEST_MAX_ANIMALS:
                break

        return detail_urls

    def _get_data_from_url(self, url):
        if url in dict(self.data.URL_REWRITES):
            url = dict(self.data.URL_REWRITES)[url]
            print "Url rewrited to '%s'" % url
        data = super(ShelterImporterTester, self)._get_data_from_url(url)
        return data

    def _get_animal(self, url):
        animal = super(ShelterImporterTester, self)._get_animal(url)
        print "Testing animal data..."

        excluded_keys = ["url"]

        for key, val in animal.items():

            if key in excluded_keys:
                continue

            test_name = 'test_animal_%s_%s_%s_%s' % (utils.name_from_url(self.url), utils.name_from_url_rest(self.url), key, self.__get_hash(url))
            if hasattr(DetailParserTest, test_name):
                print "detail UZ MA TEST!"
                exit()
            test_value = self.data.ANIMALS[url][key]
            test = test_generator_equal(test_value, val)
            # print "Adding test '%s'%s: %s" % (test_name, key, test_value)
            setattr(DetailParserTest, test_name, test)
        return animal

    def __generate_hash(self, url):
        h = hashlib.md5(url)
        return h.hexdigest()


class DetailParserTest(unittest.TestCase):
    pass


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
    print "==Setting up..."
    for shelter in SHELTERS:

        if SHELTER_ID is not None and shelter['shelter_id'] != SHELTER_ID:
            continue

        for import_url in shelter['urls']:
            try:
                importer = ShelterImporterTester(import_url, utils.name_from_url(import_url))
                print importer

                counter = 0
                for animal in importer.iter_animals():
                    # print "----Animal: %s" % animal
                    counter += 1
                    if counter >= TEST_MAX_ANIMALS:
                        break
            except ImportError:
                print "====== SKIPPING %s - no test data! ======" % import_url
            except Exception as e:
                print "Error: %s" % e
                print traceback.format_exc()
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
        print "Set shelter_id to %d" % SHELTER_ID
        del sys.argv[1:]

    unittest.main(defaultTest='suite')

