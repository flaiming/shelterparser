#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import datetime
import traceback
from bs4 import BeautifulSoup
import lxml  # needed by BeautifulSoup with features="xml"
import logging
logger = logging.getLogger(__name__)

from parsers import HtmlParser, RssParser, DetailParser
from utils import unite_url
from openers import Opener
from enums import DataType, AnimalState


def setup_logger(logger, stream, filename=None, fmt=None):
    """Sets up a logger (if no handlers exist) for console output,
    and file 'tee' output if desired."""
    if len(logger.handlers) < 1:
        console = logging.StreamHandler(stream)
        console.setLevel(logging.DEBUG)
        console.setFormatter(logging.Formatter(fmt))
        logger.addHandler(console)
        logger.setLevel(logging.DEBUG)

        if filename:
            outfile = logging.FileHandler(filename)
            outfile.setLevel(logging.INFO)
            outfile.setFormatter(logging.Formatter("%(asctime)s " + (fmt if fmt else '%(message)s')))
            logger.addHandler(outfile)


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
    },
    {
        "shelter_id": 3,
        "shelter_name": u"Centrum pro zvířata v nouzi při ZOO Liberec",
        "shelter_url": "http://www.zooliberec.cz/archa/",
        "data_type": DataType.HTML,
        "urls": {
            "http://www.zooliberec.cz/archa/cz/utulek/psi/mali-psi": AnimalState.ADOPTION,
            "http://www.zooliberec.cz/archa/cz/utulek/psi/velci-psi": AnimalState.ADOPTION,
            "http://www.zooliberec.cz/archa/cz/utulek/psi/male-feny": AnimalState.ADOPTION,
            "http://www.zooliberec.cz/archa/cz/utulek/psi/velke-feny": AnimalState.ADOPTION,
            "http://www.zooliberec.cz/archa/cz/utulek/kocky/utulkova-nabidka": AnimalState.ADOPTION,
        }
    },
    {
        "shelter_id": 4,
        "shelter_name": u"Azylpes Krásný Les u Frýdlantu (LOZ)",
        "shelter_url": "http://azylpes.cz/",
        "data_type": DataType.HTML,
        "urls": {
            "http://azylpes.cz/zvirata": AnimalState.ADOPTION,
        }
    },
    {
        "shelter_id": 5,
        "shelter_name": u"Útulek Sedliště",
        "shelter_url": "http://www.utulekpropsy.org/",
        "data_type": DataType.HTML,
        "urls": {
            "http://www.utulekpropsy.org/nabidka-psu.html": AnimalState.ADOPTION,
        }
    },
    {
        "shelter_id": 6,
        "shelter_name": u"Psí útulek Ciboušov - Klášterec nad Ohří",
        "shelter_url": "http://www.pejsciklasterec.cz/",
        "data_type": DataType.HTML,
        "urls": {
            "http://www.pejsciklasterec.cz/index.php/nabidka-pejsku/aktualne-v-utulku": AnimalState.ADOPTION,
        }
    },
]


class ShelterImporter(object):

    def __init__(self, url):
        self.url = url

    def iter_animals(self, from_date=None):
        for detail_url in self._iter_detail_urls():
            logger.debug("Detail url: %s" % (detail_url,))
            animal = self._get_animal(detail_url)

            if animal.is_satisfactory():
                if from_date is not None and not isinstance(from_date, datetime.date):
                    raise Exception("Parameter from_date is not instance of datetime.date!")
                elif from_date is not None and animal.get('date_created').date() < from_date:
                    logger.debug("Animal has been already imported (created %s)" % animal.get('date_created'))
                    return
                else:
                    yield animal.get_dict()
            else:
                logger.debug("Animal data not satisfactory --> skipping. %s" % animal.get_dict())

    def _get_animal(self, url):
        html = self._get_data_from_url(url)
        detail = DetailParser(html, url)
        animal = detail.get_animal()
        animal.set('url', url)
        return animal

    def _iter_detail_urls(self, first_page_only=False):
        parser = self._get_parser(self.url)
        for page_url in parser.get_pages():
            if page_url != self.url:
                # init parser for new page
                parser = self._get_parser(page_url)
            logger.debug("Opened page url: '%s'" % page_url)
            for detail_url in parser.get_urls():
                yield unite_url(self.url, detail_url)
            if first_page_only:
                break

    def _get_parser(self, url):
        data = self._get_data_from_url(url)

        # get content type by examining root element
        soup = BeautifulSoup(data, features="xml")
        content_type = ""
        for root in soup.children:
            if root.name:
                content_type = root.name.lower()

        if content_type == "rss":
            return RssParser(data, url)
        else:
            # default is HTML
            return HtmlParser(data, url)

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
                logger.debug("Started importer: %s", importer)

                animal_generator = importer.iter_animals(self.from_date)
                while True:
                    try:
                        animal = next(animal_generator)
                        animal['shelter_id'] = shelter['shelter_id']
                        animal['state'] = animal_state
                        yield animal
                    except StopIteration:
                        logger.debug("Catched StopIteration.")
                        break
                    except Exception:
                        logger.exception("!!! Catched exceptioni !!!")
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

    setup_logger(logger, sys.stdout)

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
