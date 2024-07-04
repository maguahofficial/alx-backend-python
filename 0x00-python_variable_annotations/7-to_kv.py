#!/usr/bin/env python3
'''a complex types - string and int/float to tuple '''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''this funct convert a key and value to a tuple of a key and the squar
    of its value '''

    return (k, float(v**2))
