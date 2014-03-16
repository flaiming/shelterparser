# Shelter parser

Parser for Czech animal shelters.

Currently parsing animals from shelters:
- http://nadace-tlapka.cz/
- http://www.mpb.cz/
- http://www.zooliberec.cz/archa/cz/utulek

This parser is used at [NajdiMazla.cz](http://najdimazla.cz).

## Installation

```bash
$ pip install -r requirements.txt
$ ./setup.py install
```

## Basic usage

```python
#!/usr/bin/env python
from shelterparser.importers import AnimalImporter

# import all animals and don't throw any exceptions
importer = AnimalImporter()

# in case of problem at importing, animal is skipped
for animal in importer.iter_animals():
    # do something with imported animal
    pass
```

## Advanced usage

```python
#!/usr/bin/env python
import datetime
from shelterparser.importers import AnimalImporter

# import animals from given date and throw exceptions
importer = AnimalImporter(from_date=datetime.date(2014, 3, 15), throw_exceptions=True)
# inicialize list of used animal shelters
shelters = AnimalImporter.get_shelters()

# generating animals one by one so we can catch exceptions
animal_generator = importer.iter_animals()
while True:
    try:
        animal = next(animal_generator)
        shelter = shelters[animal['shelter_id']]
        # do something with imported animal
    except StopIteration:
        break
    except:
        # process exception of currently imported animal
        pass
```

## Changelog

- 16.3.2014 Added import from http://www.zooliberec.cz/archa/cz/utulek

## License: Attribution-NonCommercial 3.0

© 2014 [Vojtěch Oram](http://vojtechoram.cz)
