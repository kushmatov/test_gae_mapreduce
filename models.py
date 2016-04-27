# coding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

from google.appengine.ext import ndb
from google.appengine.ext.db import NotSavedError, Key


class FakeModel(ndb.Model):
    qu = ndb.StringProperty(indexed=False)
    text = ndb.StringProperty(indexed=False)
    len = ndb.IntegerProperty(default=0)
