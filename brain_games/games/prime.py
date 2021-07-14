#!/usr/bin/env python
from math import sqrt
import random


MIN_NUM = -100
MAX_NUM = 500
TASK_DESCRIPTION = ('Answer "yes" if given number is prime. '
                    'Otherwise answer "no".')


def is_prime(number):
    if number <= 1:
        return False

    # check divisibility up to square of the number
    for divider in range(2, int(sqrt(number)) + 1):
        if number % divider == 0:
            return False
    return True


def get_task():
    number = random.randint(MIN_NUM, MAX_NUM)
    answer = 'yes' if is_prime(number) else 'no'
    return number, answer
