# -*- coding: utf-8 -*-

from .push import Push

class Kahuna(object):
    """
    Class for creating pushes
    """

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    def create_push(self):
        return Push(self)


