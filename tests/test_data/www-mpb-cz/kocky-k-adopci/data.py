import datetime

URL_REWRITES = [('http://www.mpb.cz/kocky-k-adopci/',
  'test_data/www-mpb-cz/kocky-k-adopci/file_1.html'),
 ('http://www.mpb.cz/kocky-k-adopci/?tx_odmpbrno%5Buid%5D=3878',
  'test_data/www-mpb-cz/kocky-k-adopci/file_2.html'),
 ('http://www.mpb.cz/kocky-k-adopci/?tx_odmpbrno%5Buid%5D=3853',
  'test_data/www-mpb-cz/kocky-k-adopci/file_3.html'),
 ('http://www.mpb.cz/kocky-k-adopci/?tx_odmpbrno%5Buid%5D=3854',
  'test_data/www-mpb-cz/kocky-k-adopci/file_4.html'),
 ('http://www.mpb.cz/kocky-k-adopci/?tx_odmpbrno%5Buid%5D=3847',
  'test_data/www-mpb-cz/kocky-k-adopci/file_5.html'),
 ('http://www.mpb.cz/kocky-k-adopci/?tx_odmpbrno%5Buid%5D=3756',
  'test_data/www-mpb-cz/kocky-k-adopci/file_6.html')]
ANIMALS = {'http://www.mpb.cz/kocky-k-adopci/?tx_odmpbrno%5Buid%5D=3756': {'birth_date': datetime.date(2009, 1, 3),
                                                                 'category': u'cat',
                                                                 'chip_num': '',
                                                                 'colour': u'hn\u011bd\xfd tygr',
                                                                 'date_created': datetime.datetime(2014, 1, 3, 0, 0),
                                                                 'gender': 'FEMALE',
                                                                 'name': u'evropsk\xe1',
                                                                 'note': '',
                                                                 'photos': ['http://www.mpb.cz/uploads/tx_odmpbrno/images/thumbs/4a4de8a125de5a8ccd971ccb5cb175af.jpg'],
                                                                 'reg_num': u'0003/2014',
                                                                 'street': u'ul.Eli\u0161ky Machov\xe9',
                                                                 'url': 'http://www.mpb.cz/kocky-k-adopci/?tx_odmpbrno%5Buid%5D=3756',
                                                                 'weight': 3},
 'http://www.mpb.cz/kocky-k-adopci/?tx_odmpbrno%5Buid%5D=3847': {'birth_date': datetime.date(2006, 2, 11),
                                                                 'category': u'cat',
                                                                 'chip_num': '',
                                                                 'colour': u'\u010dernob\xedl\xe1',
                                                                 'date_created': datetime.datetime(2014, 2, 10, 0, 0),
                                                                 'gender': 'MALE',
                                                                 'name': u'evropsk\xe1',
                                                                 'note': '',
                                                                 'photos': ['http://www.mpb.cz/uploads/tx_odmpbrno/images/thumbs/784061afa0c29f25e7b5524047b52dc7.jpg'],
                                                                 'reg_num': u'0023/2014',
                                                                 'street': u'ul. Gellnerova',
                                                                 'url': 'http://www.mpb.cz/kocky-k-adopci/?tx_odmpbrno%5Buid%5D=3847',
                                                                 'weight': 4},
 'http://www.mpb.cz/kocky-k-adopci/?tx_odmpbrno%5Buid%5D=3853': {'birth_date': datetime.date(2008, 2, 13),
                                                                 'category': u'cat',
                                                                 'chip_num': '',
                                                                 'colour': u'mramorovan\xe1, b\xedl\xe9 znaky',
                                                                 'date_created': datetime.datetime(2014, 2, 12, 0, 0),
                                                                 'gender': 'FEMALE',
                                                                 'name': u'k\u0159\xed\u017eenec angorsk\xe9 ko\u010dky',
                                                                 'note': '',
                                                                 'photos': ['http://www.mpb.cz/uploads/tx_odmpbrno/images/thumbs/7374e4a73f4617727bf2a99b669e0e16.jpg'],
                                                                 'reg_num': u'0026/2014',
                                                                 'street': u'ul.Krom\u011b\u0159\xed\u017esk\xe1',
                                                                 'url': 'http://www.mpb.cz/kocky-k-adopci/?tx_odmpbrno%5Buid%5D=3853',
                                                                 'weight': 3},
 'http://www.mpb.cz/kocky-k-adopci/?tx_odmpbrno%5Buid%5D=3854': {'birth_date': datetime.date(2008, 2, 13),
                                                                 'category': u'cat',
                                                                 'chip_num': '',
                                                                 'colour': u'b\xedl\xe1, tygrovan\xe9 znaky',
                                                                 'date_created': datetime.datetime(2014, 2, 12, 0, 0),
                                                                 'gender': 'MALE',
                                                                 'name': u'evropsk\xe1',
                                                                 'note': '',
                                                                 'photos': ['http://www.mpb.cz/uploads/tx_odmpbrno/images/thumbs/2b102bae6c7db1fad12f95ea20ddfd42.jpg'],
                                                                 'reg_num': u'0025/2014',
                                                                 'street': u'ul.Krom\u011b\u0159\xed\u017esk\xe1',
                                                                 'url': 'http://www.mpb.cz/kocky-k-adopci/?tx_odmpbrno%5Buid%5D=3854',
                                                                 'weight': 3},
 'http://www.mpb.cz/kocky-k-adopci/?tx_odmpbrno%5Buid%5D=3878': {'birth_date': datetime.date(2010, 2, 20),
                                                                 'category': u'cat',
                                                                 'chip_num': '',
                                                                 'colour': u'\u010dernob\xedl\xe1',
                                                                 'date_created': datetime.datetime(2014, 2, 19, 0, 0),
                                                                 'gender': 'FEMALE',
                                                                 'name': u'evropsk\xe1',
                                                                 'note': u'kastr\xe1t',
                                                                 'photos': ['http://www.mpb.cz/uploads/tx_odmpbrno/images/thumbs/bf38ad3fe876c46772d6c4a91abdf138.jpg'],
                                                                 'reg_num': u'0033/2014',
                                                                 'street': u'n\xe1m.Karla IV',
                                                                 'url': 'http://www.mpb.cz/kocky-k-adopci/?tx_odmpbrno%5Buid%5D=3878',
                                                                 'weight': 3}}
