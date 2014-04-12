import datetime

URL_REWRITES = [('http://www.utulekpribram.cz/index.php/psi-k-adopci',
  'test_data/www-utulekpribram-cz/indexphp-psi-k-adopci/file_1.html'),
 ('http://www.utulekpribram.cz/index.php/psi-k-adopci/163-argo-ev-c-7-14',
  'test_data/www-utulekpribram-cz/indexphp-psi-k-adopci/file_2.html'),
 ('http://www.utulekpribram.cz/index.php/psi-k-adopci/95-benik-ev-c-38-14',
  'test_data/www-utulekpribram-cz/indexphp-psi-k-adopci/file_3.html'),
 ('http://www.utulekpribram.cz/index.php/psi-k-adopci/98-bobina-ev-c-8-14',
  'test_data/www-utulekpribram-cz/indexphp-psi-k-adopci/file_4.html'),
 ('http://www.utulekpribram.cz/index.php/psi-k-adopci/100-david-ev-c-3-14',
  'test_data/www-utulekpribram-cz/indexphp-psi-k-adopci/file_5.html'),
 ('http://www.utulekpribram.cz/index.php/psi-k-adopci/117-fido-ev-c-12-14',
  'test_data/www-utulekpribram-cz/indexphp-psi-k-adopci/file_6.html')]
ANIMALS = {'http://www.utulekpribram.cz/index.php/psi-k-adopci/100-david-ev-c-3-14': {'birth_date': datetime.date(2004, 4, 12),
                                                                            'breed': u'k\u0159\xed\u017eenec jezev\u010d\xedka',
                                                                            'category': u'dog',
                                                                            'chip_num': '',
                                                                            'colour': '',
                                                                            'gender': 'MALE',
                                                                            'name': u'David ev.\u010d. 3/14',
                                                                            'note': u'Dav\xeddek je k ciz\xedm lidem ned\u016fv\u011b\u0159iv\xfd. Nem\xe1 r\xe1d vod\xedtko, obojek nebo jin\xe9 omezov\xe1n\xed.',
                                                                            'photos': ['http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/David/David%20(1).jpg',
                                                                                       'http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/David/David%20(2).jpg',
                                                                                       'http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/David/David%20(3).jpg',
                                                                                       'http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/David/David%20(4).jpg',
                                                                                       'http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/David/David%20(5).jpg'],
                                                                            'reg_num': u'3/14',
                                                                            'street': '',
                                                                            'url': 'http://www.utulekpribram.cz/index.php/psi-k-adopci/100-david-ev-c-3-14'},
 'http://www.utulekpribram.cz/index.php/psi-k-adopci/117-fido-ev-c-12-14': {'birth_date': datetime.date(2008, 4, 12),
                                                                            'breed': u'k\u0159\xed\u017eenec',
                                                                            'category': u'dog',
                                                                            'chip_num': '',
                                                                            'colour': '',
                                                                            'gender': 'MALE',
                                                                            'name': u'Fido ev.\u010d. 12/14',
                                                                            'note': u'Fido byl dne 29.10.2013 um\xedst\u011bn MP do z\xe1chytn\xe9ho kotce. Je to cca 6 let star\xfd k\u0159\xed\u017eenec. Je to mil\xfd, hodn\xfd a poslu\u0161n\xfd pejsek. Je pozorn\xfd a sv\xe9mu majiteli bude skv\u011bl\xfdm spole\u010dn\xedkem.',
                                                                            'photos': ['http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/Vlastik/Vlastik%20(1).jpg',
                                                                                       'http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/Vlastik/Vlastik%20(2).jpg',
                                                                                       'http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/Vlastik/Vlastik%20(3).jpg',
                                                                                       'http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/Vlastik/Vlastik%20(4).jpg',
                                                                                       'http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/Vlastik/Vlastik%20(5).jpg'],
                                                                            'reg_num': u'12/14',
                                                                            'street': '',
                                                                            'url': 'http://www.utulekpribram.cz/index.php/psi-k-adopci/117-fido-ev-c-12-14'},
 'http://www.utulekpribram.cz/index.php/psi-k-adopci/163-argo-ev-c-7-14': {'birth_date': datetime.date(2008, 10, 12),
                                                                           'breed': u'k\u0159\xed\u017eenec staforda',
                                                                           'category': u'dog',
                                                                           'chip_num': '',
                                                                           'colour': '',
                                                                           'gender': 'MALE',
                                                                           'name': u'Argo ev.\u010d. 7/14',
                                                                           'note': u'Argou\u0161ek je cca 3 let\xfd k\u0159\xed\u017eenec z\u0159ejm\u011b americk\xe9ho staford\u0161\xedrsk\xe9ho teri\xe9ra. V \xfatulku je ji\u017e p\u0159es dva roky. Dlouho nechodil na proch\xe1zky, proto\u017ee byl probl\xe9m jej postrojit, necht\u011bl nosit ko\u0161\xedk ani obojek, necht\u011bl b\xfdt p\u0159ipnut\xfd na vod\xedtku. V prosinci lo\u0148sk\xe9ho roku vy\u0161el po v\xedce ne\u017e dvou letech na svou prvn\xed proch\xe1zku. Nejprve se mu to nel\xedbilo, sna\u017eil se d\xe1t najevo, \u017ee ven j\xedt nechce, \u017ee nechce b\xfdt p\u0159ipnut\xfd a chce zp\xe1tky. Po chv\xedli ale \xfapln\u011b zapomn\u011bl, co cht\u011bl a pozorn\u011b sledoval, kam se jde. Ka\u017edou dal\u0161\xed proch\xe1zkou se velice zlep\u0161oval a i nad\xe1le zlep\u0161uje. Nyn\xed se ji\u017e t\u011b\u0161\xed ven, u\u017e se ani neot\xe1\u010d\xed zp\xe1tky k \xfatulku, nek\u0148u\u010d\xed, nebru\u010d\xed, je to velice pozorn\xfd a vn\xedmav\xfd a hlavn\u011b poslu\u0161n\xfd pes. Argou\u0161ek je p\u0159\xe1telsk\xfd pes, ale pot\u0159ebuje p\xe1n\xed\u010dka, kter\xfd mu bude rozum\u011bt. Nen\xed to pes, kter\xfd by sn\xe1\u0161el klasick\xfd cvi\u010d\xe1kov\xfd dril, rozumn\xfdm a p\u0159\xe1telsk\xfdm p\u0159\xedstupem se s n\xedm ale d\u011blaj\xed velik\xe9 pokroky a on r\xe1d poslechne na ka\u017ed\xe9 slovo. Je to pes, kter\xfd z\u0159ejm\u011b neza\u017eil moc dobr\xe9ho, ale nyn\xed ji\u017e v\u0161em ukazuje, \u017ee um\xed b\xfdt ten nejlep\u0161\xed kamar\xe1d. Za pi\u0161kot um\xed obl\xedznout cel\xfd obli\u010dej \uf04a Argou\u0161ek je kastrovan\xfd a musel mu b\xfdt amputovan\xfd oc\xe1sek.',
                                                                           'photos': ['http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/Argo/Argo%20(1).jpg',
                                                                                      'http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/Argo/Argo%20(2).jpg',
                                                                                      'http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/Argo/Argo%20(3).jpg',
                                                                                      'http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/Argo/Argo%20(4).jpg',
                                                                                      'http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/Argo/Argo%20(5).jpg'],
                                                                           'reg_num': u'7/14',
                                                                           'street': '',
                                                                           'url': 'http://www.utulekpribram.cz/index.php/psi-k-adopci/163-argo-ev-c-7-14'},
 'http://www.utulekpribram.cz/index.php/psi-k-adopci/95-benik-ev-c-38-14': {'birth_date': datetime.date(2004, 4, 12),
                                                                            'breed': u'jezev\u010d\xedk',
                                                                            'category': u'dog',
                                                                            'chip_num': '',
                                                                            'colour': '',
                                                                            'gender': 'MALE',
                                                                            'name': u'Ben\xedk ev.\u010d. 38/14',
                                                                            'note': u'Ben\xedk je cca 10 let star\xfd jezev\u010d\xedk, odchycen byl dne 17.1.2014 v B\u0159eznick\xe9 ulici. Je to velice mil\xfd pejsek.',
                                                                            'photos': ['http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/Benik/Benik%20(1).jpg',
                                                                                       'http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/Benik/Benik%20(2).jpg',
                                                                                       'http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/Benik/Benik%20(3).jpg',
                                                                                       'http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/Benik/Benik%20(4).jpg',
                                                                                       'http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/Benik/Benik%20(5).jpg'],
                                                                            'reg_num': u'38/14',
                                                                            'street': '',
                                                                            'url': 'http://www.utulekpribram.cz/index.php/psi-k-adopci/95-benik-ev-c-38-14'},
 'http://www.utulekpribram.cz/index.php/psi-k-adopci/98-bobina-ev-c-8-14': {'birth_date': datetime.date(2004, 4, 12),
                                                                            'breed': u'k\u0159\xed\u017eenec',
                                                                            'category': u'dog',
                                                                            'chip_num': '',
                                                                            'colour': '',
                                                                            'gender': 'FEMALE',
                                                                            'name': u'Bobina ev.\u010d. 8/14',
                                                                            'note': u'Bobina je cca 10 let star\xe1 fene\u010dka k\u0159\xed\u017eence. Um\xedst\u011bna byla dne 22.8.2013 MP do z\xe1chytn\xe9ho kotce. Je to mil\xe1 postar\u0161\xed d\xe1ma, r\xe1da se mazl\xed a je vd\u011b\u010dn\xe1 za ka\u017edou dobrotu a pohlazen\xed. Bylo by hezk\xe9, kdyby mohla do\u017e\xedt sv\u016fj \u017eivot s miluj\xedc\xed rodinou.',
                                                                            'photos': ['http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/Bobina/Bobina%20(1).jpg',
                                                                                       'http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/Bobina/Bobina%20(2).jpg',
                                                                                       'http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/Bobina/Bobina%20(3).jpg',
                                                                                       'http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/Bobina/Bobina%20(4).jpg',
                                                                                       'http://www.utulekpribram.cz/images/Psi%20k%20adopci/max/Bobina/Bobina%20(5).jpg'],
                                                                            'reg_num': u'8/14',
                                                                            'street': '',
                                                                            'url': 'http://www.utulekpribram.cz/index.php/psi-k-adopci/98-bobina-ev-c-8-14'}}
