# coding: utf-8
from __future__ import unicode_literals


VERSION = (2, 17, 0)


def get_version(version=VERSION):
    return '.'.join(map(str, version))


__version__ = get_version(VERSION)
