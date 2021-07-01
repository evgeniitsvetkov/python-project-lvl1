#!/usr/bin/env python
import math
import random

import brain_games.games.flow as flow


task = 'Find the greatest common divisor of given numbers.'


def get_question():
    min_num = 1
    max_num = 100
    a = random.randint(min_num, max_num)
    b = random.randint(min_num, max_num)
    question = f'{a} {b}'
    return question


def get_answer(question):
    a, b = [int(x) for x in question.split()]
    return str(math.gcd(a, b))


def brain_gcd():
    flow.game_flow(task, get_question, get_answer)
