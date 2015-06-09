from __future__ import unicode_literals
from builtins import object, str
import datetime
from types import NoneType


class AnimalModel(object):
    """
    Base model class for storing data about animal
    """

    fields = {
        'original_id': str,
        'reg_num': str,
        'name': str,
        'chip_num': str,
        'date_created': datetime.datetime,
        'street': str,
        'gender': str,
        'category': str,
        'birth_date': datetime.date,
        'colour': str,
        'height': int,
        'weight': int,
        'note': str,
        'vaccinated': bool,
        'castrated': bool,
        'dewormed': bool,
        'chipped': bool,
        'handicapped': bool,
        'photos': list,
        'breed': str,
        'url': str,
        'state': str,
    }

    def set(self, field, value):
        # print "Setting %s to %s of type %s" % (field, value, type(value))
        if field not in list(self.fields.keys()):
            raise AttributeError("Animal do not have field '%s'!" % field)
        if isinstance(value, NoneType):
            return
        if not isinstance(value, self.fields[field]):
            raise TypeError("Field '%s' has to be type '%s', not '%s'!" % (field, self.fields[field], type(value)))
        setattr(self, field, value)

    def get(self, field):
        if field in self.fields and hasattr(self, field):
            return getattr(self, field)
        raise AttributeError("Animal do not have field '%s'!" % field)

    def get_dict(self):
        result = {}
        for field in self.fields:
            if hasattr(self, field):
                result[field] = getattr(self, field)
        return result

    def is_satisfactory(self):
        """
        Checks if animal has minimal required attributes
        """
        obligatory_attrs = ['category', 'gender', 'photos', 'date_created']
        for attr in obligatory_attrs:
            if not hasattr(self, attr):
                return False
        return True
