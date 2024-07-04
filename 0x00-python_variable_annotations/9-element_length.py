#!/usr/bin/env python3
'''  Let's duck type a iterable object '''

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''this fuction computes the length of a list of sequences.
    '''
    return [(i, len(i)) for i in lst]
