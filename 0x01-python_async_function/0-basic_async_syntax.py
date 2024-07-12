#!/usr/bin/env python3
'''
the module for task 0
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' this functionWaits for a random number of seconds. '''
    wait_timex = random.random() * max_delay
    await asyncio.sleep(wait_timex)
    return wait_timex
