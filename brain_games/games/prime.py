#!/usr/bin/env python
from math import sqrt
import random


MIN_NUM = 1
MAX_NUM = 500


task_description = ('Answer "yes" if given number is prime. '
                    'Otherwise answer "no".')


def get_prime_numbers(max_number=500):
    first_prime_number = 2
    prime_numbers = [first_prime_number]

    # check only odd numbers
    for number in range(3, max_number + 1, 2):
        is_prime = True
        # check divisibility up to square of the number
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                is_prime = False
        if is_prime:
            prime_numbers.append(number)
    return prime_numbers


def get_task():
    number = random.randint(MIN_NUM, MAX_NUM)
    prime_numbers = get_prime_numbers()
    answer = 'yes' if number in prime_numbers else 'no'
    return number, answer
