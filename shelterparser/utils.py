import re
import datetime


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
    raw_parts = date.split(u'.')
    parts = []
    for i in range(len(raw_parts)):
        try:
            parts.append(int(re.sub(ur'\D+', '', raw_parts[i])))
        except ValueError:
            pass
    if len(parts) == 3:
        if int(parts[0]) > 1990:
            return datetime.datetime(parts[0], parts[1], parts[2])
        elif int(parts[2]) > 1990:
            return datetime.datetime(parts[2], parts[1], parts[0])
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
    return ""


def name_from_url(url):
    return url.split('/')[2].replace('.', '-')


def name_from_url_rest(url):
    if url.startswith('http'):
        part = '-'.join(filter(None, url.split('/')[3:]))
    else:
        part = '-'.join(filter(None, url.split('/')[1:]))
    return re.sub(r'[^a-z0-9_-]+', '', part)
