# -*- coding: utf-8 -*-
import re
import datetime

RE_MONTHS = (
    (ur"\bLed(?:en|n(?:a|u|e|em))\b", 1),
    (ur"\bÚnor(?:a|u|e|em)?\b", 2),
    (ur"\bBřez(?:en|n(?:a|u|e|em))\b", 3),
    (ur"\bDub(?:en|n(?:a|u|e|em))\b", 4),
    (ur"\bKvět(?:en|n(?:a|u|e|em))\b", 5),
    (ur"\bČerv(?:en|n(?:a|u|e|em))\b", 6),
    (ur"\bČerven(?:ec|c(?:i|e|em))\b", 7),
    (ur"\bSrp(?:en|n(?:a|u|e|em))\b", 8),
    (ur"\bZáří", 9),
    (ur"\bŘíj(?:en|n(?:a|u|e|em))\b", 10),
    (ur"\bListopad(?:u|e|em)?\b", 11),
    (ur"\bProsin(?:ec|c(?:i|e|em))\b", 12),
)


def unite_url(base_url, url):
    if url.startswith('http'):
        return url
    base_url = get_base_url(base_url)
    if url.startswith('/'):
        return "/".join(base_url.split('/')[:3]) + url
    else:
        return "%s/%s" % (base_url if not base_url.endswith('/') else base_url[:-1], url)


def get_base_url(url):
    if not url.startswith('http'):
        return url
    domain = url
    # cut off GET parameters
    index = url.find('?')
    if index >= 0:
        domain = domain[:index]
    part_count = len(domain.split('/'))
    return "/".join(domain.split('/')[:-1]) if part_count > 3 else domain


def get_domain_from_url(url):
    if not url.startswith('http'):
        return ""
    return url.split('/')[2]


def parse_date(date):
    # search for standart time devider (.|/)
    raw_parts = re.split(u'\.|/', date)
    if len(raw_parts) > 1:
        parts = []
        for i in range(len(raw_parts)):
            try:
                parts.append(int(re.sub(ur'\D+', '', raw_parts[i])))
            except ValueError:
                pass
        if len(parts) >= 3:
            if int(parts[0]) > 1990:
                return datetime.date(parts[0], parts[1], parts[2])
            elif int(parts[2]) > 1990:
                return datetime.date(parts[2], parts[1], parts[0])
        elif parts[1] > 1990 and parts[0] in range(1, 13):
            return datetime.date(parts[1], parts[0], 1)
    else:
        # search for month name
        month = None
        year = None
        for month_re, month_num in RE_MONTHS:
            if re.match(month_re, date, flags=re.I | re.U):
                month = month_num
        # search for year
        result = re.findall(ur"\d{4}", date)
        if result:
            year_raw = int(result[0])
            # validate year
            if year_raw > 1960 and year_raw < 2050:
                year = year_raw
        if year:
            return datetime.date(year, month if month else 1, 1)
    return None


def parse_time(time):
    parts = time.split(':')
    if len(parts) > 1:
        for i in range(len(parts)):
            parts[i] = int(re.sub(ur'\D+', '', parts[i]))
        return (parts[0], parts[1])
    return (0, 0)


def parse_bool(str_val):
    if re.match(ur'ano', str_val, flags=re.I | re.U):
        return True
    elif re.match(ur'ne', str_val, flags=re.I | re.U):
        return False
    return None


def name_from_url(url):
    return url.split('/')[2].replace('.', '-')


def name_from_url_rest(url):
    if url.startswith('http'):
        part = '-'.join(filter(None, url.split('/')[3:]))
    else:
        part = '-'.join(filter(None, url.split('/')[1:]))
    return re.sub(r'[^a-z0-9_-]+', '', part)
