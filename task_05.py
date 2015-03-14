#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Just a Docstring"""

MYLIST = [(1,2,3),'A,B,C']

def flip_keys(to_flip):
    counter = 0
    for value in to_flip:
        to_flip[counter] = value[::-1]
        counter += 1
    return to_flip
