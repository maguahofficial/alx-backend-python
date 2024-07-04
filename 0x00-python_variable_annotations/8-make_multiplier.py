#!/usr/bin/env python3
''' a complex types - functions '''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''this funct multiplies a float by the multiplier '''

    return lambda x: x * multiplier
