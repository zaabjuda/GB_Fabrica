# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"


class LimitExceeded(Exception):
    def __init__(self, limit):
        self.limit = limit
