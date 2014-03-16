import datetime

URL_REWRITES = [('http://www.mpb.cz/psi-k-adopci/',
  'test_data/www-mpb-cz/psi-k-adopci/file_1.html'),
 ('http://www.mpb.cz/psi-k-adopci/?tx_odmpbrno%5Buid%5D=3908',
  'test_data/www-mpb-cz/psi-k-adopci/file_2.html'),
 ('http://www.mpb.cz/psi-k-adopci/?tx_odmpbrno%5Buid%5D=3901',
  'test_data/www-mpb-cz/psi-k-adopci/file_3.html'),
 ('http://www.mpb.cz/psi-k-adopci/?tx_odmpbrno%5Buid%5D=3899',
  'test_data/www-mpb-cz/psi-k-adopci/file_4.html'),
 ('http://www.mpb.cz/psi-k-adopci/?tx_odmpbrno%5Buid%5D=3894',
  'test_data/www-mpb-cz/psi-k-adopci/file_5.html'),
 ('http://www.mpb.cz/psi-k-adopci/?tx_odmpbrno%5Buid%5D=3892',
  'test_data/www-mpb-cz/psi-k-adopci/file_6.html')]
ANIMALS = {'http://www.mpb.cz/psi-k-adopci/?tx_odmpbrno%5Buid%5D=3892': {'birth_date': datetime.date(2004, 2, 24),
                                                               'category': u'dog',
                                                               'chip_num': '',
                                                               'colour': u'kr\xe9mov\xe1',
                                                               'date_created': datetime.datetime(2014, 2, 23, 0, 0),
                                                               'gender': 'FEMALE',
                                                               'height': 34,
                                                               'name': u'k\u0159\xed\u017eenec',
                                                               'note': '',
                                                               'photos': ['http://www.mpb.cz/uploads/tx_odmpbrno/images/thumbs/fd50ffbff92cac11d2319c31b9d768f7.jpg'],
                                                               'reg_num': u'0141/2014',
                                                               'street': u'ul.\u0160v\xe9dsk\xe1',
                                                               'url': 'http://www.mpb.cz/psi-k-adopci/?tx_odmpbrno%5Buid%5D=3892',
                                                               'weight': 9},
 'http://www.mpb.cz/psi-k-adopci/?tx_odmpbrno%5Buid%5D=3894': {'birth_date': datetime.date(2013, 2, 24),
                                                               'category': u'dog',
                                                               'chip_num': '',
                                                               'colour': u'\u010dern\xe1 a p\xe1len\xedm',
                                                               'date_created': datetime.datetime(2014, 2, 24, 0, 0),
                                                               'gender': 'MALE',
                                                               'height': 59,
                                                               'name': u'k\u0159\xed\u017eenec n\u011bmeck\xe9ho ov\u010d\xe1ka',
                                                               'note': u'',
                                                               'photos': ['http://www.mpb.cz/uploads/tx_odmpbrno/images/thumbs/5bfef4e2c3e8cb9d85009c4866521f7f.jpg'],
                                                               'reg_num': u'0145/2014',
                                                               'street': u'ul. Podb\u011blohorsk\xe1',
                                                               'url': 'http://www.mpb.cz/psi-k-adopci/?tx_odmpbrno%5Buid%5D=3894',
                                                               'weight': 23},
 'http://www.mpb.cz/psi-k-adopci/?tx_odmpbrno%5Buid%5D=3899': {'birth_date': datetime.date(2013, 2, 26),
                                                               'category': u'dog',
                                                               'chip_num': '',
                                                               'colour': u'\u017elut\xe1',
                                                               'date_created': datetime.datetime(2014, 2, 26, 0, 0),
                                                               'gender': 'FEMALE',
                                                               'height': 55,
                                                               'name': u'k\u0159\xed\u017eenec',
                                                               'note': u'',
                                                               'photos': ['http://www.mpb.cz/uploads/tx_odmpbrno/images/thumbs/3d1cd53dcbdab7411f1617ee8d8130d6.jpg'],
                                                               'reg_num': u'0150/2014',
                                                               'street': u'ul. U Anton\xed\u010dka',
                                                               'url': 'http://www.mpb.cz/psi-k-adopci/?tx_odmpbrno%5Buid%5D=3899',
                                                               'weight': 16},
 'http://www.mpb.cz/psi-k-adopci/?tx_odmpbrno%5Buid%5D=3901': {'birth_date': datetime.date(2013, 10, 31),
                                                               'category': u'dog',
                                                               'chip_num': '',
                                                               'colour': u'\u010dern\xe1, b\xedl\xe9 znaky',
                                                               'date_created': datetime.datetime(2014, 2, 28, 0, 0),
                                                               'gender': 'MALE',
                                                               'height': 37,
                                                               'name': u'k\u0159\xed\u017eenec',
                                                               'note': u'',
                                                               'photos': ['http://www.mpb.cz/uploads/tx_odmpbrno/images/thumbs/b34583272dfc1673ae2ef7ac48002cc1.jpg'],
                                                               'reg_num': u'0152/2014',
                                                               'street': u'\u010cerven\xfd kopec',
                                                               'url': 'http://www.mpb.cz/psi-k-adopci/?tx_odmpbrno%5Buid%5D=3901',
                                                               'weight': 7},
 'http://www.mpb.cz/psi-k-adopci/?tx_odmpbrno%5Buid%5D=3908': {'birth_date': datetime.date(2011, 3, 3),
                                                               'category': u'dog',
                                                               'chip_num': '',
                                                               'colour': u'vlko\u0161ed\xe1',
                                                               'date_created': datetime.datetime(2014, 3, 2, 0, 0),
                                                               'gender': 'FEMALE',
                                                               'height': 60,
                                                               'name': u'alja\u0161sk\xfd malamut',
                                                               'note': '',
                                                               'photos': ['http://www.mpb.cz/uploads/tx_odmpbrno/images/thumbs/9ee4e29db6f85fcfa7f9b010edb976f8.jpg'],
                                                               'reg_num': u'0164/2014',
                                                               'street': u'vr\xe1cena schovatelem',
                                                               'url': 'http://www.mpb.cz/psi-k-adopci/?tx_odmpbrno%5Buid%5D=3908',
                                                               'weight': 36}}
