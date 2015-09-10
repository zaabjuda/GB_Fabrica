# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"


from strictdict import StrictDict
from strictdict import fields as f


class GuestBookMessageData(StrictDict):
    message = f.String(required=True)
    author_id = f.Int(required=True)


class GuestBookCreateData(StrictDict):
    name = f.String(required=True)
    slug = f.String(required=True)
    is_moderated = f.Bool(required=False)
