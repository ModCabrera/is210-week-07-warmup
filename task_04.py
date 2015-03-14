#!/urs/bin/env python
# -*- coding: utf-8 -*-
"""Module Receives Data and returns SUM,Average of list or tuples"""


def process_data(numlist):
    """Does some math on list and returns a tuple.

    Args:
    numlist: List values arithmetically increment and average concat with comma.
    
    Returns:
    tupl: Arguments concatenated with commas.

    Examples:
    >>> process_data([1,2,3])
    (6, 2.0)

    >>> process_data([5,6,7])
    (18, 6.0)
    """
    total = 0
    for value in numlist:
        total += value
    return total, (total/float(len(numlist)))
