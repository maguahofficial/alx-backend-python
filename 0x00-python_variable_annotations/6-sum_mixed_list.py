#!/usr/bin/env python3
''' a complex types - mixed list
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' unction sums a list of floats and integers. '''

    return float(sum(mxd_lst))
