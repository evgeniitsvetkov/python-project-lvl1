#!/usr/bin/env python
import random


MIN_NUM = 1
MAX_NUM = 100
TASK_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(num_a, num_b):
    # Euclidean algorithm
    while num_a != 0 and num_b != 0:
        if num_a > num_b:
            num_a = num_a % num_b
        else:
            num_b = num_b % num_a
    return num_a + num_b


def get_task():
    num_a = random.randint(MIN_NUM, MAX_NUM)
    num_b = random.randint(MIN_NUM, MAX_NUM)
    question = f'{num_a} {num_b}'
    answer = str(gcd(num_a, num_b))
    return question, answer
