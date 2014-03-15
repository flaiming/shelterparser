#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import datetime
import traceback
from bs4 import BeautifulSoup
import lxml  # needed by BeautifulSoup with features="xml"

from parsers import HtmlParser, RssParser, DetailParser
from utils import unite_url
from openers import Opener
from enums import DataType, AnimalState


SHELTERS = [
    {
        "shelter_id": 1,
        "shelter_name": u"Útulek pro opuštěná zvířata MP Brno",
        "shelter_url": "http://www.mpb.cz/",
        "data_type": DataType.HTML,
        "urls": {
            "http://www.mpb.cz/nalezeni-psi/": AnimalState.FOUND,
            "http://www.mpb.cz/nalezene-kocky/": AnimalState.FOUND,
            "http://www.mpb.cz/psi-k-adopci/": AnimalState.ADOPTION,
            "http://www.mpb.cz/kocky-k-adopci/": AnimalState.ADOPTION,
        }
    },
    {
        "shelter_id": 2,
        "shelter_name": u"Nadace Tlapka",
        "shelter_url": "http://nadace-tlapka.cz/",
        "data_type": DataType.HTML,
        "urls": {
            "http://nadace-tlapka.cz/nabidka-zvirat/": AnimalState.ADOPTION,
        }
    }
]


class ShelterImporter(object):

    def __init__(self, url):
        self.url = url

    def iter_animals(self, from_date=None):
        for detail_url in self._iter_detail_urls():
            print "Detail url: %s" % (detail_url,)
            animal = self._get_animal(detail_url)

            if from_date and isinstance(from_date, datetime.datetime) and animal['date_created'] < from_date:
                return
            else:
                yield animal

    def _get_animal(self, url):
        html = self._get_data_from_url(url)
        detail = DetailParser(html, url)
        animal = detail.get_animal().get_dict()
        animal['url'] = url
        return animal

    def _iter_detail_urls(self):
        parser = self._get_parser(self.url)
        for page_url in parser.get_pages():
            if page_url != self.url:
                # init parser for new page
                parser = self._get_parser(page_url)
            print "Opened page url: '%s'" % page_url
            for detail_url in parser.get_urls():
                yield unite_url(self.url, detail_url)

    def _get_parser(self, url):
        data = self._get_data_from_url(url)

        # get content type by examining root element
        soup = BeautifulSoup(data, features="xml")
        content_type = ""
        for root in soup.children:
            if root.name:
                content_type = root.name.lower()

        if content_type == "html":
            return HtmlParser(data, url)
        elif content_type == "rss":
            return RssParser(data, url)
        else:
            raise Exception("Unknown content type '%s'!" % content_type)

    def _get_data_from_url(self, url):
        return Opener(url).read()

    def __str__(self):
        return "Importer with URL '%s'." % self.url


class AnimalImporter(object):

    def __init__(self, from_date=None, throw_exceptions=False):
        self.from_date = from_date
        self.throw_exceptions = throw_exceptions

    def iter_animals(self):
        for shelter in SHELTERS:
            for import_url, animal_state in shelter['urls'].items():
                importer = ShelterImporter(import_url)
                print importer

                animal_generator = importer.iter_animals(self.from_date)
                while True:
                    try:
                        animal = next(animal_generator)
                        animal['shelter_id'] = shelter['shelter_id']
                        animal['state'] = animal_state
                        yield animal
                    except StopIteration:
                        print "Catched StopIteration."
                        break
                    except Exception as e:
                        print "===== Catched exception: %s" % e
                        print traceback.format_exc()
                        if self.throw_exceptions:
                            raise

    @staticmethod
    def get_shelters():
        shelters = {}
        for shelter in SHELTERS:
            shelters[shelter['shelter_id']] = {
                "name": shelter['shelter_name'],
                "url": shelter['shelter_url'],
            }
        return shelters


def main():
    from_date = datetime.datetime.now()
    if len(sys.argv) >= 2:
        from_date = sys.argv[1]
        try:
            parts = from_date.split('-')
            from_date = datetime.datetime(int(parts[0]), int(parts[1]), int(parts[2]))
        except:
            print "Wrong date! Use format YYYY-MM-DD"
            return False
    else:
        print """
        Please run with date from which you want animals
        $ importers.py YYYY-MM-DD
        """
        return False

    importer = AnimalImporter(from_date)
    for animal in importer.iter_animals():
        print "---Animal: %s" % animal

    # opener = TarGzOpener('./test_data/kocky-online.cz/data.tar.gz', "windows-1250")
    # importer = KockyOnlineImporter(opener)
    # for animal in importer.iter_animals():
    #     pprint.pprint(animal.get_dict())
    #     print ','


if __name__ == '__main__':
    main()
