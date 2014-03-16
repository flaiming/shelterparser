import datetime

URL_REWRITES = [('http://www.zooliberec.cz/archa/cz/utulek/kocky/utulkova-nabidka',
  'test_data/www-zooliberec-cz/archa-cz-utulek-kocky-utulkova-nabidka/file_1.html'),
 ('http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2042&page=0&catid=6&Itemid=147',
  'test_data/www-zooliberec-cz/archa-cz-utulek-kocky-utulkova-nabidka/file_2.html'),
 ('http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2033&page=0&catid=6&Itemid=147',
  'test_data/www-zooliberec-cz/archa-cz-utulek-kocky-utulkova-nabidka/file_3.html'),
 ('http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2031&page=0&catid=6&Itemid=147',
  'test_data/www-zooliberec-cz/archa-cz-utulek-kocky-utulkova-nabidka/file_4.html'),
 ('http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2032&page=0&catid=6&Itemid=147',
  'test_data/www-zooliberec-cz/archa-cz-utulek-kocky-utulkova-nabidka/file_5.html'),
 ('http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2034&page=0&catid=6&Itemid=147',
  'test_data/www-zooliberec-cz/archa-cz-utulek-kocky-utulkova-nabidka/file_6.html')]
ANIMALS = {'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2031&page=0&catid=6&Itemid=147': {'birth_date': datetime.date(2012, 1, 25),
                                                                                                                 'category': u'cat',
                                                                                                                 'chip_num': '',
                                                                                                                 'colour': '',
                                                                                                                 'date_created': datetime.datetime(2014, 1, 24, 0, 0),
                                                                                                                 'gender': 'FEMALE',
                                                                                                                 'name': u'Ad\xe9lka',
                                                                                                                 'note': '',
                                                                                                                 'photos': ['http://www.zooliberec.cz/archa/images/reference/14l14adelka4.jpg',
                                                                                                                            'http://www.zooliberec.cz/archa/images/reference/14l14adelka2.jpg',
                                                                                                                            'http://www.zooliberec.cz/archa/images/reference/14l14adelka.jpg'],
                                                                                                                 'reg_num': '',
                                                                                                                 'street': '',
                                                                                                                 'url': 'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2031&page=0&catid=6&Itemid=147'},
 'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2032&page=0&catid=6&Itemid=147': {'category': u'cat',
                                                                                                                 'chip_num': '',
                                                                                                                 'colour': '',
                                                                                                                 'date_created': datetime.datetime(2014, 1, 24, 0, 0),
                                                                                                                 'gender': 'MALE',
                                                                                                                 'name': u'Kuba',
                                                                                                                 'note': '',
                                                                                                                 'photos': ['http://www.zooliberec.cz/archa/images/reference/13l14kuba2.jpg',
                                                                                                                            'http://www.zooliberec.cz/archa/images/reference/13l14kuba.jpg'],
                                                                                                                 'reg_num': '',
                                                                                                                 'street': '',
                                                                                                                 'url': 'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2032&page=0&catid=6&Itemid=147'},
 'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2033&page=0&catid=6&Itemid=147': {'birth_date': datetime.date(2009, 1, 24),
                                                                                                                 'category': u'cat',
                                                                                                                 'chip_num': '',
                                                                                                                 'colour': '',
                                                                                                                 'date_created': datetime.datetime(2014, 1, 24, 0, 0),
                                                                                                                 'gender': 'MALE',
                                                                                                                 'name': u'Tom',
                                                                                                                 'note': '',
                                                                                                                 'photos': ['http://www.zooliberec.cz/archa/images/reference/11l14tom.jpg'],
                                                                                                                 'reg_num': '',
                                                                                                                 'street': '',
                                                                                                                 'url': 'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2033&page=0&catid=6&Itemid=147'},
 'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2034&page=0&catid=6&Itemid=147': {'birth_date': datetime.date(2010, 1, 25),
                                                                                                                 'category': u'cat',
                                                                                                                 'chip_num': '',
                                                                                                                 'colour': '',
                                                                                                                 'date_created': datetime.datetime(2014, 1, 24, 0, 0),
                                                                                                                 'gender': 'MALE',
                                                                                                                 'name': u'Honz\xedk',
                                                                                                                 'note': '',
                                                                                                                 'photos': ['http://www.zooliberec.cz/archa/images/reference/10l14.jpg'],
                                                                                                                 'reg_num': '',
                                                                                                                 'street': '',
                                                                                                                 'url': 'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2034&page=0&catid=6&Itemid=147'},
 'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2042&page=0&catid=6&Itemid=147': {'birth_date': datetime.date(2013, 2, 15),
                                                                                                                 'category': u'cat',
                                                                                                                 'chip_num': '',
                                                                                                                 'colour': '',
                                                                                                                 'date_created': datetime.datetime(2014, 2, 15, 0, 0),
                                                                                                                 'gender': 'FEMALE',
                                                                                                                 'name': u'St\xe1\u010fa',
                                                                                                                 'note': '',
                                                                                                                 'photos': ['http://www.zooliberec.cz/archa/images/reference/19l14stada.jpg'],
                                                                                                                 'reg_num': '',
                                                                                                                 'street': '',
                                                                                                                 'url': 'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2042&page=0&catid=6&Itemid=147'}}
