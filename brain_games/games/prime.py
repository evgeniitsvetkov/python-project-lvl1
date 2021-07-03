#!/usr/bin/env python
from math import gcd
import random


MIN_NUM = -100
MAX_NUM = 500


task_description = ('Answer "yes" if given number is prime. '
                    'Otherwise answer "no".')


def get_task():
    number = random.randint(MIN_NUM, MAX_NUM)

    is_prime = True
    if number > 1:
        for i in range(2, number):
            if gcd(i, number) != 1:
                is_prime = False
    else:
        is_prime = False

    answer = 'yes' if is_prime else 'no'
    return number, answer
