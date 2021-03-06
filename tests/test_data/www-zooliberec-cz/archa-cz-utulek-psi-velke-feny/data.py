import datetime

URL_REWRITES = [('http://www.zooliberec.cz/archa/cz/utulek/psi/velke-feny',
  'test_data/www-zooliberec-cz/archa-cz-utulek-psi-velke-feny/file_1.html'),
 ('http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2057&page=0&catid=4&Itemid=140',
  'test_data/www-zooliberec-cz/archa-cz-utulek-psi-velke-feny/file_2.html'),
 ('http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=1854&page=0&catid=4&Itemid=140',
  'test_data/www-zooliberec-cz/archa-cz-utulek-psi-velke-feny/file_3.html'),
 ('http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=401&page=0&catid=4&Itemid=140',
  'test_data/www-zooliberec-cz/archa-cz-utulek-psi-velke-feny/file_4.html')]
ANIMALS = {'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=1854&page=0&catid=4&Itemid=140': {'birth_date': datetime.date(2009, 3, 14),
                                                                                                                 'breed': u'k\u0159\xed\u017eenec',
                                                                                                                 'category': u'dog',
                                                                                                                 'chip_num': '',
                                                                                                                 'colour': '',
                                                                                                                 'date_created': datetime.datetime(2013, 9, 12, 0, 0),
                                                                                                                 'gender': 'FEMALE',
                                                                                                                 'name': u'Venou\u0161ka',
                                                                                                                 'note': '',
                                                                                                                 'photos': ['http://www.zooliberec.cz/archa/images/reference/img_2654.jpg',
                                                                                                                            'http://www.zooliberec.cz/archa/images/reference/img_2649.jpg',
                                                                                                                            'http://www.zooliberec.cz/archa/images/reference/img_2650.jpg',
                                                                                                                            'http://www.zooliberec.cz/archa/images/reference/236l13venouska5.jpg'],
                                                                                                                 'reg_num': '',
                                                                                                                 'street': '',
                                                                                                                 'url': 'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=1854&page=0&catid=4&Itemid=140'},
 'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2057&page=0&catid=4&Itemid=140': {'birth_date': datetime.date(2008, 11, 9),
                                                                                                                 'breed': u'NO',
                                                                                                                 'category': u'dog',
                                                                                                                 'chip_num': '',
                                                                                                                 'colour': '',
                                                                                                                 'date_created': datetime.datetime(2013, 11, 9, 0, 0),
                                                                                                                 'gender': 'FEMALE',
                                                                                                                 'name': u'Bora',
                                                                                                                 'note': '',
                                                                                                                 'photos': ['http://www.zooliberec.cz/archa/images/reference/309l14bora4.jpg',
                                                                                                                            'http://www.zooliberec.cz/archa/images/reference/309l13bora5.jpg',
                                                                                                                            'http://www.zooliberec.cz/archa/images/reference/309l13bora2.jpg',
                                                                                                                            'http://www.zooliberec.cz/archa/images/reference/309l13bora.jpg',
                                                                                                                            'http://www.zooliberec.cz/archa/images/reference/309l13bora3.jpg'],
                                                                                                                 'reg_num': '',
                                                                                                                 'street': '',
                                                                                                                 'url': 'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=2057&page=0&catid=4&Itemid=140'},
 'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=401&page=0&catid=4&Itemid=140': {'birth_date': datetime.date(2005, 8, 1),
                                                                                                                'breed': u'k\u0159\xed\u017eenec ov\u010d\xe1ka',
                                                                                                                'category': u'dog',
                                                                                                                'chip_num': '',
                                                                                                                'colour': '',
                                                                                                                'date_created': datetime.datetime(2010, 8, 1, 0, 0),
                                                                                                                'gender': 'FEMALE',
                                                                                                                'name': u'F\xedna',
                                                                                                                'note': '',
                                                                                                                'photos': ['http://www.zooliberec.cz/archa/images/reference/fina3.jpg',
                                                                                                                           'http://www.zooliberec.cz/archa/images/reference/fina2.jpg',
                                                                                                                           'http://www.zooliberec.cz/archa/images/reference/fina.jpg',
                                                                                                                           'http://www.zooliberec.cz/archa/images/reference/fina4.jpg'],
                                                                                                                'reg_num': '',
                                                                                                                'street': '',
                                                                                                                'url': 'http://www.zooliberec.cz/archa/index.php?option=com_reference&view=single&id=401&page=0&catid=4&Itemid=140'}}
