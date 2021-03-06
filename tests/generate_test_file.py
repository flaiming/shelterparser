#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from builtins import str
from builtins import range
import os
import io
import sys
import argparse
import importlib
import pprint
import traceback
# added parent path so we can import shelterparser module
sys.path.append(os.path.abspath('..'))

from shelterparser import utils
from shelterparser.importers import ShelterImporter
from shelterparser.openers import Opener

GENERATE_MAX_ANIMALS = 5


class ShelterImporterTestGenerator(ShelterImporter):

    def __init__(self, url, default, folder, regenerate):
        super(ShelterImporterTestGenerator, self).__init__(url, default)
        self.folder = folder
        self.regenerate = regenerate
        self.url_rewrites = []
        self.animals = {}
        self.counter = 1

        if self.regenerate:
            data = importlib.import_module("test_data.%s.%s.data" % (utils.name_from_url(url), utils.name_from_url_rest(url)))
            print("Imported data: %s" % data)
            self.url_rewrites = data.URL_REWRITES
            self.animals = data.ANIMALS
        else:
            # create folder if not exists
            if not os.path.exists(folder):
                os.makedirs(folder)
                # create __init__.py
                open(os.path.join(folder, "__init__.py"), 'a').close()

    def _iter_detail_urls(self):
        for url in super(ShelterImporterTestGenerator, self)._iter_detail_urls():
            print("URL: %s" % url)
            yield url

    def _get_data_from_url(self, url):
        data = ""
        if self.regenerate:
            file_path = dict(self.url_rewrites)[url]
            print("File path: %s" % file_path)
            with io.open(file_path, 'r') as f:
                data = f.read()
        else:
            opener = Opener(url)
            data = opener.read()

            file_path = self.__create_file_path("file")

            with io.open(file_path, 'w', encoding=opener.get_encoding()) as f:
                print("Writing to file %s..." % file_path)
                f.write(str(data))
                self.url_rewrites.append((url, file_path))
        return data

    def _get_animal(self, url):
        animal = super(ShelterImporterTestGenerator, self)._get_animal(url)
        print("Creating test files for animal...")
        if animal.is_satisfactory():
            self.animals[url] = animal.get_dict()
        else:
            print("Animal does not have satisfactory attributes! Removing from test files.")
            for i in range(0, len(self.url_rewrites)):
                if self.url_rewrites[i][0] == url:
                    os.remove(self.url_rewrites[i][1])
                    del self.url_rewrites[i]
                    break
        return animal

    def __create_file_path(self, base_name):
        name = "%s_%d.html" % (base_name, self.counter)
        self.counter += 1
        return os.path.join(self.folder, name)


def save_file(file_path, url_rewrites, animals):
    with io.open(file_path, 'w', encoding="utf-8") as f:
        print("Writing to file %s..." % file_path)
        f.write(u"import datetime\n\n")
        f.write("URL_REWRITES = %s\n" % str(pprint.pformat(url_rewrites)))
        f.write("ANIMALS = %s\n" % str(pprint.pformat(animals)))


def init_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        # create __init__.py
        open(os.path.join(folder, "__init__.py"), 'a').close()


def main():
    test_folder = "test_data"
    url = ""

    parser = argparse.ArgumentParser(description='Generate test files for given shelter URL.')
    parser.add_argument('url', help='URL of shelter with animal list.')
    parser.add_argument('-r', '--regenerate', action='store_true', help='regenerate current tests using already downloaded files.')
    parser.add_argument('-g', '--gender', help='default gender')
    parser.add_argument('-c', '--category', help='default category')

    args = parser.parse_args()

    default = {}
    if args.gender:
        default['gender'] = args.gender
    if args.category:
        default['category'] = args.category

    url = args.url
    regenerate = args.regenerate
    print("Processing url '%s'..." % (url))
    try:

        # create folder if not exists
        root_folder = os.path.join(test_folder, utils.name_from_url(url))
        init_folder(root_folder)

        importer = ShelterImporterTestGenerator(url, default, os.path.join(root_folder, utils.name_from_url_rest(url)), regenerate=regenerate)
        print(importer)

        generated_animals = 0
        try:
            for animal in importer.iter_animals():
                print("Imported animal: %s" % animal)
                generated_animals += 1
                if generated_animals >= GENERATE_MAX_ANIMALS:
                    break
        except KeyboardInterrupt:
            pass
        save_file(os.path.join(test_folder, utils.name_from_url(url), utils.name_from_url_rest(url), "data.py"), importer.url_rewrites, importer.animals)
        print("Successfully generated tests for %d animals for URL '%s'." % (generated_animals, url))
    except IOError as e:
        print("Cannot open URL %s: %s" % (url, e.strerror))
        traceback.print_exc()
        exit(1)


if __name__ == '__main__':
    main()

