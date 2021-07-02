#!/usr/bin/env python
import math
import random


MIN_NUM = 1
MAX_NUM = 100


task_description = 'Find the greatest common divisor of given numbers.'


def get_task():
    a = random.randint(MIN_NUM, MAX_NUM)
    b = random.randint(MIN_NUM, MAX_NUM)
    question = f'{a} {b}'
    answer = str(math.gcd(a, b))
    return question, answer
