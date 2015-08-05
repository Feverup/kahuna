# -*- coding: utf-8 -*-


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


