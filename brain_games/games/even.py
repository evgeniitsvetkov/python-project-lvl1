#!/usr/bin/env python
import random


MIN_NUM = 1
MAX_NUM = 100


task_description = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_task():
    number = random.randint(MIN_NUM, MAX_NUM)
    answer = 'yes' if number % 2 == 0 else 'no'
    return number, answer
