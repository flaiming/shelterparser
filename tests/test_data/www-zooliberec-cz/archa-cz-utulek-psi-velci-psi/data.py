import datetime

URL_REWRITES = [('http://www.zooliberec.cz/archa/cz/utulek/psi/velci-psi',
  'test_data/www-zooliberec-cz/archa-cz-utulek-psi-velci-psi/file_1.html'),
 ('http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2051&page=0&catid=3&Itemid=139',
  'test_data/www-zooliberec-cz/archa-cz-utulek-psi-velci-psi/file_2.html'),
 ('http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2050&page=0&catid=3&Itemid=139',
  'test_data/www-zooliberec-cz/archa-cz-utulek-psi-velci-psi/file_3.html'),
 ('http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2044&page=0&catid=3&Itemid=139',
  'test_data/www-zooliberec-cz/archa-cz-utulek-psi-velci-psi/file_4.html'),
 ('http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2040&page=0&catid=3&Itemid=139',
  'test_data/www-zooliberec-cz/archa-cz-utulek-psi-velci-psi/file_5.html'),
 ('http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2011&page=0&catid=3&Itemid=139',
  'test_data/www-zooliberec-cz/archa-cz-utulek-psi-velci-psi/file_6.html')]
ANIMALS = {'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2011&page=0&catid=3&Itemid=139': {'birth_date': datetime.date(2009, 1, 24),
                                                                                                                 'category': u'dog',
                                                                                                                 'chip_num': '',
                                                                                                                 'colour': '',
                                                                                                                 'date_created': datetime.datetime(2014, 1, 24, 0, 0),
                                                                                                                 'gender': 'MALE',
                                                                                                                 'name': u'Harty',
                                                                                                                 'note': '',
                                                                                                                 'photos': ['http://www.zooliberec.cz/archa/images/reference/29hr14harty2.jpg',
                                                                                                                            'http://www.zooliberec.cz/archa/images/reference/29hr14harty.jpg',
                                                                                                                            'http://www.zooliberec.cz/archa/images/reference/29hr14harty3.jpg',
                                                                                                                            'http://www.zooliberec.cz/archa/images/reference/29hr14harty4.jpg',
                                                                                                                            'http://www.zooliberec.cz/archa/images/reference/29hr14harty5.jpg'],
                                                                                                                 'reg_num': '',
                                                                                                                 'street': '',
                                                                                                                 'url': 'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2011&page=0&catid=3&Itemid=139'},
 'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2040&page=0&catid=3&Itemid=139': {'birth_date': datetime.date(2013, 2, 5),
                                                                                                                 'category': u'dog',
                                                                                                                 'chip_num': '',
                                                                                                                 'colour': '',
                                                                                                                 'date_created': datetime.datetime(2014, 2, 5, 0, 0),
                                                                                                                 'gender': 'MALE',
                                                                                                                 'name': u'Nezmar',
                                                                                                                 'note': '',
                                                                                                                 'photos': ['http://www.zooliberec.cz/archa/images/reference/42l14nezmar.jpg',
                                                                                                                            'http://www.zooliberec.cz/archa/images/reference/42l14nezmar2.jpg',
                                                                                                                            'http://www.zooliberec.cz/archa/images/reference/42l14nezmar4.jpg',
                                                                                                                            'http://www.zooliberec.cz/archa/images/reference/42l14nezmar3.jpg'],
                                                                                                                 'reg_num': '',
                                                                                                                 'street': '',
                                                                                                                 'url': 'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2040&page=0&catid=3&Itemid=139'},
 'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2044&page=0&catid=3&Itemid=139': {'birth_date': datetime.date(2011, 8, 12),
                                                                                                                 'category': u'dog',
                                                                                                                 'chip_num': '',
                                                                                                                 'colour': '',
                                                                                                                 'date_created': datetime.datetime(2014, 2, 10, 0, 0),
                                                                                                                 'gender': 'MALE',
                                                                                                                 'name': u'Bady',
                                                                                                                 'note': '',
                                                                                                                 'photos': ['http://www.zooliberec.cz/archa/images/reference/120l13bady.jpg',
                                                                                                                            'http://www.zooliberec.cz/archa/images/reference/120l13bady2.jpg',
                                                                                                                            'http://www.zooliberec.cz/archa/images/reference/120l13bady3.jpg'],
                                                                                                                 'reg_num': '',
                                                                                                                 'street': '',
                                                                                                                 'url': 'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2044&page=0&catid=3&Itemid=139'},
 'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2050&page=0&catid=3&Itemid=139': {'birth_date': datetime.date(2012, 8, 24),
                                                                                                                 'category': u'dog',
                                                                                                                 'chip_num': '',
                                                                                                                 'colour': '',
                                                                                                                 'date_created': datetime.datetime(2014, 2, 22, 0, 0),
                                                                                                                 'gender': 'MALE',
                                                                                                                 'name': u'Ignor',
                                                                                                                 'note': '',
                                                                                                                 'photos': ['http://www.zooliberec.cz/archa/images/reference/53l14ignor3.jpg',
                                                                                                                            'http://www.zooliberec.cz/archa/images/reference/53l14ignor2.jpg',
                                                                                                                            'http://www.zooliberec.cz/archa/images/reference/53l14ignor.jpg'],
                                                                                                                 'reg_num': '',
                                                                                                                 'street': '',
                                                                                                                 'url': 'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2050&page=0&catid=3&Itemid=139'},
 'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2051&page=0&catid=3&Itemid=139': {'birth_date': datetime.date(2010, 2, 28),
                                                                                                                 'category': u'dog',
                                                                                                                 'chip_num': '',
                                                                                                                 'colour': '',
                                                                                                                 'date_created': datetime.datetime(2014, 2, 27, 0, 0),
                                                                                                                 'gender': 'MALE',
                                                                                                                 'name': u'Dan',
                                                                                                                 'note': '',
                                                                                                                 'photos': ['http://www.zooliberec.cz/archa/images/reference/26l09dan.jpg',
                                                                                                                            'http://www.zooliberec.cz/archa/images/reference/26l09dan3.jpg',
                                                                                                                            'http://www.zooliberec.cz/archa/images/reference/26l09.jpg'],
                                                                                                                 'reg_num': '',
                                                                                                                 'street': '',
                                                                                                                 'url': 'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2051&page=0&catid=3&Itemid=139'}}
