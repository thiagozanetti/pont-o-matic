#! /usr/bin/env python

import settings

"""
Sends messages to console
"""
def log(message):
    if settings.debug:
        print(message)

