#!urs/bin/env python
# -*- coding: utf-8 -*-
"""Module Receives Data and returns SUM,Average of list or tuples"""


def process_data(numlist):
    total = 0
    for i in numlist:
        total += numlist[0:]
        return total
    return numlist


NUMLIST = [1,2,3]

SUMUP = sum(NUMLIST[0:])

AVG = float(SUMUP) / len(NUMLIST[0:])
