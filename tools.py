# coding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

from models import DataModel, FakeModel
from mapreduce import operation as op
from google.appengine.api import search
from random import randrange as rnd

NAMES = [u'Кирилл', u'Игорь', u'Вася', u'Саша', u'Олег', u'Илья', u'Ваня', u'Варя']
LN = len(NAMES)


def validator(prms):
    prms['count'] = int(prms['count'])
    prms['string_length'] = int(prms['string_length'])


def addfake(entity):
    name = NAMES[rnd(LN)] + ' ' + (entity if rnd(2) else '')
    my_document = search.Document(
        # Setting the doc_id is optional. If omitted, the search service will create an identifier.
        fields=[
            search.TextField(name='customer', value=name),
            search.HtmlField(name='comment', value='dddf  ' + entity),
        ],
        language='ru'
    )
    search.Index('testing').put(my_document)

    yield op.counters.Increment('fakes')


def chekfake(entity):
    na = NAMES[rnd(LN)]
    r = search.Index('testing').search(na)
    f = FakeModel(qu=na, text=str(r))
    yield op.db.Put(f)
    yield op.counters.Increment('searchs')


