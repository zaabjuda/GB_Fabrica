# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"


from strictdict import StrictDict
from strictdict import fields as f


class GuestBookMessageData(StrictDict):
    message = f.String(required=True)
    author_id = f.Int(required=True)
