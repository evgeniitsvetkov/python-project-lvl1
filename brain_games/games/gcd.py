#!/usr/bin/env python
import math
import random


MIN_NUM = 1
MAX_NUM = 100


task = 'Find the greatest common divisor of given numbers.'


def get_question():
    a = random.randint(MIN_NUM, MAX_NUM)
    b = random.randint(MIN_NUM, MAX_NUM)
    question = f'{a} {b}'
    return question


def get_answer(question):
    a, b = [int(x) for x in question.split()]
    return str(math.gcd(a, b))
