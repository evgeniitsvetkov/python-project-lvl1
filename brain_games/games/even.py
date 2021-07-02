#!/usr/bin/env python
import random


MIN_NUM = 1
MAX_NUM = 100


task = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    number_to_guess = random.randint(MIN_NUM, MAX_NUM)
    return number_to_guess


def get_answer(number_to_guess):
    if number_to_guess % 2 == 0:
        return 'yes'
    else:
        return 'no'
