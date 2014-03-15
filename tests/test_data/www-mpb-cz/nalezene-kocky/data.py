import datetime

URL_REWRITES = [('http://www.mpb.cz/nalezene-kocky/',
  'test_data/www-mpb-cz/nalezene-kocky/file_1.html'),
 ('http://www.mpb.cz/nalezene-kocky/?tx_odmpbrno%5Buid%5D=3902',
  'test_data/www-mpb-cz/nalezene-kocky/file_2.html')]
ANIMALS = {'http://www.mpb.cz/nalezene-kocky/?tx_odmpbrno%5Buid%5D=3902': {'birth_date': datetime.date(2010, 3, 1),
                                                                 'category': u'cat',
                                                                 'chip_num': '',
                                                                 'colour': u'\u010dernob\xedl\xe1',
                                                                 'date_created': datetime.datetime(2014, 2, 28, 0, 0),
                                                                 'gender': 'FEMALE',
                                                                 'name': u'evropsk\xe1',
                                                                 'note': u'kastrovan\xe1',
                                                                 'photos': ['http://www.mpb.cz/uploads/tx_odmpbrno/images/thumbs/245731898629c111fc559f5b2a54ba02.jpg'],
                                                                 'reg_num': u'0037/2014',
                                                                 'street': u'ul.Sv\xe1\u017en\xe1',
                                                                 'url': 'http://www.mpb.cz/nalezene-kocky/?tx_odmpbrno%5Buid%5D=3902',
                                                                 'weight': 3}}
