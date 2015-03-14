#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module Tests Lists with Nested Immutable Values"""


def flip_keys(to_flip):
    """ Takes a list, and returns it reversed, tests mutability.

    Args:
    to_flip: Reverses immutable sequences in lists elements.

    Returns:
    list: Arguments with inner elements reversed.

    Examples:
    
    >>> flip_keys([(1,2,3),'A,B,C'])
    [(3, 2, 1), 'C,B,A']

    >>> flip_keys([(1,2,3),'R,E,T,T,E,B,G,N,I,L,E,E,F,M,I'])
    [(3, 2, 1), 'I,M,F,E,E,L,I,N,G,B,E,T,T,E,R']
    """
    counter = 0
    for value in to_flip:
        to_flip[counter] = value[::-1]
        counter += 1
    return to_flip
