#!/usr/bin/env python
import random


MIN_NUM = 1
MAX_NUM = 100


task_description = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    # Euclidean algorithm
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def get_task():
    a = random.randint(MIN_NUM, MAX_NUM)
    b = random.randint(MIN_NUM, MAX_NUM)
    question = f'{a} {b}'
    answer = str(gcd(a, b))
    return question, answer
