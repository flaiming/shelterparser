import datetime

URL_REWRITES = [('http://nadace-tlapka.cz/nabidka-zvirat/',
  'test_data/nadace-tlapka-cz/nabidka-zvirat/file_1.html'),
 ('http://nadace-tlapka.cz/nabidka-zvirat/?nabidkaID=555',
  'test_data/nadace-tlapka-cz/nabidka-zvirat/file_2.html'),
 ('http://nadace-tlapka.cz/nabidka-zvirat/?nabidkaID=552',
  'test_data/nadace-tlapka-cz/nabidka-zvirat/file_3.html'),
 ('http://nadace-tlapka.cz/nabidka-zvirat/?nabidkaID=550',
  'test_data/nadace-tlapka-cz/nabidka-zvirat/file_4.html'),
 ('http://nadace-tlapka.cz/nabidka-zvirat/?nabidkaID=548',
  'test_data/nadace-tlapka-cz/nabidka-zvirat/file_5.html'),
 ('http://nadace-tlapka.cz/nabidka-zvirat/?nabidkaID=546',
  'test_data/nadace-tlapka-cz/nabidka-zvirat/file_6.html')]
ANIMALS = {'http://nadace-tlapka.cz/nabidka-zvirat/?nabidkaID=546': {'birth_date': datetime.date(2009, 1, 11),
                                                           'castrated': False,
                                                           'category': u'dog',
                                                           'chip_num': '',
                                                           'colour': '',
                                                           'date_created': datetime.datetime(2014, 1, 11, 0, 0),
                                                           'gender': 'MALE',
                                                           'name': u'Halder',
                                                           'note': '',
                                                           'photos': ['http://nadace-tlapka.cz/wp-content/uploads//00216.jpg'],
                                                           'reg_num': u'140009',
                                                           'street': u'Kozl\xedky',
                                                           'url': 'http://nadace-tlapka.cz/nabidka-zvirat/?nabidkaID=546'},
 'http://nadace-tlapka.cz/nabidka-zvirat/?nabidkaID=548': {'birth_date': datetime.date(2008, 1, 13),
                                                           'castrated': False,
                                                           'category': u'dog',
                                                           'chip_num': '',
                                                           'colour': '',
                                                           'date_created': datetime.datetime(2014, 1, 12, 0, 0),
                                                           'gender': 'FEMALE',
                                                           'name': u'B\xe1ra',
                                                           'note': '',
                                                           'photos': ['http://nadace-tlapka.cz/wp-content/uploads//163.jpg'],
                                                           'reg_num': u'140011',
                                                           'street': u'Teplice',
                                                           'url': 'http://nadace-tlapka.cz/nabidka-zvirat/?nabidkaID=548'},
 'http://nadace-tlapka.cz/nabidka-zvirat/?nabidkaID=550': {'birth_date': datetime.date(2008, 1, 19),
                                                           'castrated': False,
                                                           'category': u'dog',
                                                           'chip_num': '',
                                                           'colour': '',
                                                           'date_created': datetime.datetime(2014, 1, 18, 0, 0),
                                                           'gender': 'FEMALE',
                                                           'name': u'Locika',
                                                           'note': '',
                                                           'photos': ['http://nadace-tlapka.cz/wp-content/uploads//0332.jpg'],
                                                           'reg_num': u'140013',
                                                           'street': u'Hrob',
                                                           'url': 'http://nadace-tlapka.cz/nabidka-zvirat/?nabidkaID=550'},
 'http://nadace-tlapka.cz/nabidka-zvirat/?nabidkaID=552': {'birth_date': datetime.date(2012, 2, 4),
                                                           'castrated': False,
                                                           'category': u'dog',
                                                           'chip_num': '',
                                                           'colour': '',
                                                           'date_created': datetime.datetime(2014, 2, 3, 0, 0),
                                                           'gender': 'MALE',
                                                           'name': u'M\xe1rio',
                                                           'note': '',
                                                           'photos': ['http://nadace-tlapka.cz/wp-content/uploads//P2020242.jpg'],
                                                           'reg_num': u'140015',
                                                           'street': u'Krupka',
                                                           'url': 'http://nadace-tlapka.cz/nabidka-zvirat/?nabidkaID=552'},
 'http://nadace-tlapka.cz/nabidka-zvirat/?nabidkaID=555': {'birth_date': datetime.date(2013, 2, 27),
                                                           'castrated': False,
                                                           'category': u'dog',
                                                           'chip_num': '',
                                                           'colour': '',
                                                           'date_created': datetime.datetime(2014, 2, 27, 0, 0),
                                                           'gender': 'FEMALE',
                                                           'name': u'Sa\u0161a',
                                                           'note': '',
                                                           'photos': ['http://nadace-tlapka.cz/wp-content/uploads//0671.jpg'],
                                                           'reg_num': u'140018',
                                                           'street': u'Dub\xed',
                                                           'url': 'http://nadace-tlapka.cz/nabidka-zvirat/?nabidkaID=555'}}