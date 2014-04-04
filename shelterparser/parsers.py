# -*- coding: utf-8 -*-
import re
from itertools import cycle, islice
from bs4 import BeautifulSoup
import datetime
import feedparser
import difflib

from enums import CategoryType, resolve_gender_and_category
from models import AnimalModel
import utils


class Accuracy():
    LOW = 0
    NORMAL = 5
    HIGH = 10

    @classmethod
    def exists(cls, accuracy):
        attrs = dir(cls)
        for attr in attrs:
            if getattr(cls, attr) == accuracy:
                return True
        return False


class GenericParser(object):

    def __init__(self, html, url):
        self.html = html.replace('&nbsp;', ' ')
        self.html = re.sub(r'\s+', ' ', self.html)
        self.soup = BeautifulSoup(self.html)
        self.url = url
        self.base_url = self._get_base_url(url)
        self.accuracy = Accuracy.NORMAL

    def set_accuracy(self, new_accuracy):
        if not Accuracy.exists(new_accuracy):
            raise AttributeError("Accuracy value %s is not valid!" % repr(new_accuracy))
        self.accuracy = new_accuracy

    def _get_base_url(self, url):
        bases = self.soup.select("html head base")
        if bases and bases[0].has_attr('href'):
            return bases[0]['href']
        return url

    def _common_parent(self, *elements):
        """
        Finds one common parent for multiple elements.
        Pretty inefficient and dirty solution, should be remaked in the future.
        """
        parent_list = []
        # print "Found elements: %s" % repr(list(elements))
        for e in list(elements):
            if e:
                parent_list.append(list(e.parents)[:5])
        #print "parent list: %s" % repr(parent_list)
        #print "Parent list count: %d" % len(parent_list)
        for x in range(len(parent_list)):
            for y in range(len(parent_list[x])):
                successes = 0
                for xx in range(len(parent_list)):
                    for yy in range(len(parent_list[xx])):
                        if parent_list[x] != parent_list[xx]:
                            if parent_list[x][y] != parent_list[xx][yy]:
                                pass
                            else:
                                successes += 1
                                if successes >= len(parent_list) - 1:
                                    return parent_list[x][y]
        return None

    def _find_nearest_elems(self, elem, tag, id_name="", class_name="", depth=4):
        result = self.__find_nearest_descendant_elems(elem, tag, id_name, class_name)
        result = self.__filter_elements_without_text(result)
        if result:
            return result
        # search in siblings
        results = []
        for e in roundrobin(elem.previous_siblings, elem.next_siblings):
            res = self.__find_nearest_descendant_elems(e, tag, id_name=id_name, class_name=class_name)
            res = self.__filter_elements_without_text(res)
            # print "Result: %s" % repr(res)
            if res:
                for r in res:
                    results.append(r)
        if results:
            return results
        # print "Nenalezeno v sourozencich, jdu na rodice (depth=%d)" % depth
        if depth > 0:
            return self._find_nearest_elems(elem.parent, tag, id_name=id_name, class_name=class_name, depth=depth - 1)
        return []

    def __filter_elements_without_text(self, elements):
        if elements:
            return [res for res in elements if res.get_text().strip() == ""]
        return []

    def __find_nearest_descendant_elems(self, elem, tag, id_name="", class_name=""):
        if not hasattr(elem, 'name'):
            # element is probably string
            return []
        # print "Element: %s" % elem.name
        if elem.name == tag:
            if id_name == "" or elem['id'] == id_name:
                if tag == "" or (elem.has_attr('class') and class_name in elem['class']):
                    return elem
        # search in children
        if hasattr(elem, 'find_all'):
            res = elem.find_all(tag)
            if res:
                results = []
                for r in res:
                    results.append(r)
                return results
        return None

    def _find_nearest(self, elem, pattern):
        limit = 5
        for el in roundrobin([elem], elem.next_elements, elem.previous_elements):
            if hasattr(el, "get_text"):
                text = el.get_text(" ").strip()
                if not pattern.match(text) and re.sub(pattern, '', text).strip() != '':
                    return re.sub(pattern, '', text).strip()
            elif el != elem:
                return el.string.strip()
            limit -= 1
            if limit < 0:
                break
        return ""

    def _filter_siblings(self, elements, max_parent_depth=3):
        """
        Filter out non-siblings and returns siblings with greater count.
        """
        parent_list = []
        for e in elements:
            if e:
                parent_list.append(list(e.parents)[:max_parent_depth])
        element_count = len(parent_list)
        if element_count == 0:
            return []

        parent_stats = {}
        for index in range(0, element_count):
            for parent in parent_list[index]:
                if parent in parent_stats:
                    parent_stats[parent].append(elements[index])
                else:
                    parent_stats[parent] = [elements[index]]

        best_children = []
        # parents with most children first
        for k in sorted(parent_stats, key=lambda k: len(parent_stats[k]), reverse=True):
            children = parent_stats[k]
            children_ok = True
            for i in range(1, len(children)):
                if self._get_string_difference(children[i - 1]['href'], children[i]['href']) < 0.9:
                    children_ok = False
                    break
            if children_ok:
                best_children = children
                break
        return best_children

    def _get_string_difference(self, a, b):
        difference = difflib.SequenceMatcher(None, a, b).quick_ratio()
        return difference


class HtmlParser(GenericParser):

    def _check_link(self, link):
        if link['href'].startswith('http'):
            domain = utils.get_domain_from_url(link['href'])
            shelter_domain = utils.get_domain_from_url(self.url)
            # print "Comparing domains: %s vs %s" % (domain, shelter_domain)
            if domain != shelter_domain:
                # print "Discarding link %s" % link
                return False
        # remove relative links, like "./"
        return not re.match(r'\.?/', link['href'])

    def get_urls(self):
        links = []
        # first try - find links by searching for "Zobrazit vice" etc.
        for link in self.soup.find_all('a', text=re.compile(ur'^zobrazit více', flags=re.I | re.U)):
            if self._check_link(link):
                links.append(link)

        # second try - find animal links by "a img"
        if not links:
            for link in self.soup.find_all('a'):
                if link.find('img') and self._check_link(link):
                    links.append(link)
            links = self._filter_siblings(
                links,
                max_parent_depth=4
            )
            # print "Siblings: %s" % links
        # print "Links: %s" % links
        return map(lambda x: x['href'], links)

    def get_pages(self):
        siblings = self._filter_siblings(
            self.soup.find_all('a', text=re.compile(ur'^\d+$')),
            max_parent_depth=3
        )
        links = [self.url]
        for link in siblings:
            if link.string.strip() == "1":
                # URL for first link already added
                pass
            else:
                links.append(link['href'])
        return links


class RssParser(GenericParser):

    def __init__(self, xml, url):
        self.xml = xml
        self.url = url

    def get_urls(self):
        result = []
        data = feedparser.parse(self.xml)
        if 'entries' in data and len(data['entries']):
            for entry in data['entries']:
                if 'link' in entry:
                    link = entry['link']
                    result.append(link)
        return result

    def get_pages(self):
        return [self.url]


RE_DEVIDER = ur'\s*:?\s*(?:<[^>]+>\s*){0,4}\s*:?\s*'


class DetailParser(GenericParser):

    RE_DATE_CREATED = ur'(?:Datum (?:předání pejska do útulku|předání do útulku|přijetí do útulku|a čas odchytu|nálezu|přijetí|nalezení)|v útulku od)'
    RE_AGE = ur'\b(?:Stáří|Věk)\b'

    def __init__(self, html, url):
        super(DetailParser, self).__init__(html, url)
        self.fields = [
            'reg_num',
            'name',
            'chip_num',
            'date_created',
            'street',
            'gender',
            'category',
            'birth_date',
            'colour',
            'height',
            'weight',
            'note',
            'photos',
            'castrated',
            'breed',
        ]
        self.category = None

    def get_animal(self):
        animal = AnimalModel()
        for field in self.fields:
            method = getattr(self, "get_%s" % field)
            result = method()
            animal.set(field, result)

        if not animal.is_satisfactory():
            raise Exception("!!! Animal doesn't have all obligatory parameters! %s" % animal.get_dict())
        return animal

    def get_name(self):
        name = u""
        common_parent = self._get_common_parent()
        if common_parent:
            # recursively search common parent for h1,h2,h3,h4 elements
            for i in range(4):
                common_parent = common_parent.parent
                heading = common_parent.find(re.compile("^h(?:1|2|3|4)$"))
                if heading:
                    name = unicode(heading.find(text=True, recursive=False))
                    break
        return name.strip()

    def get_reg_num(self):
        result = re.findall(ur'Evidenční\s+číslo' + RE_DEVIDER + ur'([\w\d/_ -]+)', self.html, flags=re.I | re.U)
        reg_num = ""
        if result:
            reg_num = result[0].strip()
        return reg_num

    def get_chip_num(self):
        result = re.findall(ur'Č(?:íslo|\.)\s+čipu' + RE_DEVIDER + ur'(\d+)', self.html, flags=re.I | re.U)
        chip_num = ""
        if result:
            chip_num = result[0].strip()
        return chip_num

    def get_date_created(self):
        if self.accuracy == Accuracy.NORMAL:
            result = re.findall(self.RE_DATE_CREATED + RE_DEVIDER + ur'([\w\d.,: ]+)', self.html, flags=re.I | re.U)
        elif self.accuracy == Accuracy.LOW:
            result = re.findall(ur'\b\d{1,4}(?:-|\.|,)\d{1,4}(?:-|\.|,)\d{1,4}\b', self.html, flags=re.I | re.U)
        date = None
        if result:
            raw = result[0].strip()
            # remove spaces around dots
            raw = re.sub(ur'\s*(\.)\s*', r'\1', raw)
            date_date = utils.parse_date(raw)
            if date_date:
                date = datetime.datetime(date_date.year, date_date.month, date_date.day)
        return date

    def get_street(self):
        result = re.findall(ur'Místo\s+(?:odchytu|nalezení|nálezu)' + RE_DEVIDER + ur'([\w\d()., _-]+)', self.html, flags=re.I | re.U)
        street = ""
        if result:
            street = result[0].strip()
        return street

    def get_gender(self):

        if self.accuracy == Accuracy.NORMAL:
            result = re.findall(ur'Pohlaví' + RE_DEVIDER + ur'(?:<[^>]*>)?\s*(\w+)', self.html, flags=re.I | re.U)
        elif self.accuracy == Accuracy.LOW:
            result = re.findall(ur'\b(pes|kočka|kocour|fena|fenka|samec|samice)\b', self.html, flags=re.I | re.U)
        gender = None
        if result:
            raw_gender = result[0].strip()
            gender, self.category = resolve_gender_and_category(raw_gender)
        return gender

    def get_category(self):
        if self.category:
            return self.category
        else:
            # try get_gender
            self.get_gender()
            if self.category:
                return self.category
            else:
                result = re.findall(ur'Druh' + RE_DEVIDER + ur'(\w+)', unicode(self.html), flags=re.U | re.I)
                if result:
                    raw_category = result[0].strip()
                    self.category = CategoryType.resolve_category(raw_category)
                    if self.category:
                        return self.category
        return ""

    def get_birth_date(self):

        date_created = self.get_date_created()
        if not date_created:
            # we don't know from when to compute birth date
            return None

        result = re.findall(self.RE_AGE + RE_DEVIDER + ur'([\w\d.,/ -]+)', self.html, flags=re.I | re.U)
        age = None
        birth_date = None
        if result:
            raw_age = result[0].strip()
            raw_age = re.sub(ur'^[a-z]+\s*', '', raw_age, flags=re.I | re.U)
            # nejdrive zkusime najit interval
            if re.search(ur'\d+-\d+', raw_age, flags=re.I | re.U):
                result = re.findall(ur'\d+-\d+', raw_age, flags=re.I | re.U)
                if result:
                    parts = result[0].split(u'-')
                    try:
                        age = (int(parts[0]) + int(parts[1])) / 2.0
                    except ValueError:
                        pass
            elif re.search(ur'\d+(?:(?:\.|/)\d+){1,2}', raw_age):
                return utils.parse_date(raw_age)
            elif re.search(ur'\d+(?:,|\.)?\d*', raw_age, flags=re.I | re.U):  # zadano primo cislem
                result = re.findall(ur'\d+(?:,|\.)?\d*', raw_age, flags=re.I | re.U)
                if result:
                    try:
                        age = float(result[0].replace(',', '.'))
                    except ValueError:
                        pass
            if age:
                bd = datetime.date.today()
                if age > 1980:
                    # probably year of birth
                    bd = datetime.date(int(age), 1, 1)
                else:
                    # relative age
                    if u"měsíc" in raw_age and not u"rok" in raw_age:
                        # months only
                        bd = date_created.date() - datetime.timedelta(days=int(age) * 30)
                    else:
                        # year
                        days_per_year = 365.24
                        bd = date_created.date() - datetime.timedelta(days=int(days_per_year * age))
                birth_date = bd
        return birth_date

    def get_colour(self):
        result = re.findall(ur'Barva' + RE_DEVIDER + ur'([\w\d,._ -]+)', unicode(self.html), flags=re.U | re.I)
        colour = ""
        if result:
            colour = result[0].strip()
        return colour

    def get_height(self):
        result = re.findall(ur'Výška' + RE_DEVIDER + ur'([\w\d,. -]+)', self.html, flags=re.I | re.U)
        height = None
        if result:
            raw_height = result[0].strip()
            if re.search(ur'\bcm\b', raw_height, flags=re.I | re.U):
                result = re.findall(ur'\d+', raw_height, flags=re.I | re.U)
                if result:
                    try:
                        height = int(result[0])
                    except ValueError:
                        pass
        return height

    def get_weight(self):
        result = re.findall(ur'Váha' + RE_DEVIDER + ur'([\w\d,. -]+)', self.html, flags=re.I | re.U)
        weight = None
        if result:
            raw_weight = result[0].strip()
            if re.search(ur'\bkg\b', raw_weight, flags=re.I | re.U):
                result = re.findall(ur'(\d+)(?:,|\.)?\d*', raw_weight, flags=re.I | re.U)
                if result:
                    try:
                        weight = int(result[0])
                    except ValueError:
                        pass
        return weight

    def get_note(self):
        pattern = re.compile(ur'(?:Poznámky|Popis):', re.U | re.I)
        tag = self.soup.find(text=pattern)
        note = ""
        if tag:
            note = self._find_nearest(tag, pattern)
        return note

    def get_castrated(self):
        result = re.findall(ur'Kastrace' + RE_DEVIDER + ur'(\w+)', unicode(self.html), flags=re.U | re.I)
        castrated = None
        if result:
            castrated = utils.parse_bool(result[0].strip())
        return castrated

    def get_breed(self):
        result = re.findall(ur'Rasa' + RE_DEVIDER + ur'([\w,. -]+)', unicode(self.html), flags=re.U | re.I)
        breed = ""
        if result:
            breed = result[0].strip()
        return breed

    def get_photos(self):
        common_parent = self._get_common_parent()
        if common_parent:
            results = self._find_nearest_elems(common_parent, 'a', depth=5)
            photos = []
            for a in results:
                if re.match(ur'.+\.(?:jpg|jpeg|gif|png).*', a['href'], flags=re.I | re.U):
                    if a['href'].startswith('http'):
                        photos.append(a['href'].replace('\\', '/'))
                    elif a['href'].startswith('/'):
                        photos.append(utils.unite_url(self.url, a['href'].replace('\\', '/')))
                    elif a['href'].startswith('javascript'):
                        photo = re.sub(ur'[^/]*([a-z0-9/ _-]+\.(?:jpg|jpeg|gif|png))[^/]*', ur'\1', a['href'], flags=re.I | re.U)
                        if photo:
                            photo = photo.replace('\\', '/')
                            photos.append(utils.unite_url(self.base_url, photo))
                    else:
                        photos.append(utils.unite_url(self.base_url, a['href'].replace('\\', '/')))
            return photos
        return []

    def _get_common_parent(self):
        return self._common_parent(
            self.soup.find(text=re.compile(self.RE_AGE, re.U | re.I)),
            self.soup.find(text=re.compile(self.RE_DATE_CREATED, re.U | re.I))
        )


def roundrobin(*iterables):
    """roundrobin('ABC', 'D', 'EF') --> A D E B F C"""
    # Recipe credited to George Sakkis
    pending = len(iterables)
    nexts = cycle(iter(it).next for it in iterables)
    while pending:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            pending -= 1
            nexts = cycle(islice(nexts, pending))
