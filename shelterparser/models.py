import datetime
from types import NoneType


class AnimalModel():
    """
    Base model class for storing data about animal
    """

    fields = {
        'original_id': basestring,
        'reg_num': basestring,
        'name': basestring,
        'chip_num': basestring,
        'date_created': datetime.datetime,
        'street': basestring,
        'gender': basestring,
        'category': basestring,
        'birth_date': datetime.date,
        'colour': basestring,
        'height': int,
        'weight': int,
        'note': basestring,
        'vaccinated': bool,
        'castrated': bool,
        'dewormed': bool,
        'chipped': bool,
        'handicapped': bool,
        'photos': list,
        'breed': basestring,
        'url': basestring,
    }

    def set(self, field, value):
        # print "Setting %s to %s of type %s" % (field, value, type(value))
        if field not in self.fields.keys():
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
        obligatory_attrs = ['category', 'gender', 'photos']
        for attr in obligatory_attrs:
            if not hasattr(self, attr):
                return False
        return True
