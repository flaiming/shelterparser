# -*- coding: utf-8 -*-
# Enums. Attributes has to be uppercase.
from __future__ import unicode_literals
from builtins import object

import re


class GenericType(object):

    @classmethod
    def get_tuple(cls):
        result = []
        attrs = dir(cls)
        for attr in attrs:
            if re.match(ur'[A-Z]+', attr):
                result.append((attr, getattr(cls, attr)))
        return result


class DataType(GenericType):
    RSS = 'RSS'
    XML = 'XML'
    HTML = 'HTML'


class GenderType(GenericType):
    MALE = 'MALE'
    FEMALE = 'FEMALE'

    @staticmethod
    def resolve_gender(raw_gender):
        gender, _ = resolve_gender_and_category(raw_gender)
        return gender


class AnimalState(GenericType):
    NONE = "NONE"
    ADOPTION = "ADOPTION"
    FOUND = "FOUND"
    LOST = "LOST"


class CategoryType(GenericType):
    DOG = u'dog'
    CAT = u'cat'

    @staticmethod
    def resolve_category(raw_category):
        _, category = resolve_gender_and_category(raw_category)
        return category


def resolve_gender_and_category(raw_gender):
    gender_categories = {
        ur"pes": {
            "gender": GenderType.MALE,
            "category": CategoryType.DOG
        },
        ur"fenk?a": {
            "gender": GenderType.FEMALE,
            "category": CategoryType.DOG
        },
        ur"kocour": {
            "gender": GenderType.MALE,
            "category": CategoryType.CAT
        },
        ur"kočka": {
            "gender": GenderType.FEMALE,
            "category": CategoryType.CAT
        },
        ur"samec": {
            "gender": GenderType.MALE,
            "category": ""
        },
        ur"samice": {
            "gender": GenderType.FEMALE,
            "category": ""
        },
    }
    for reg, val in list(gender_categories.items()):
        if re.match(reg, raw_gender, flags=re.I | re.U):
            return (val['gender'], val['category'])
    return ('', '')

