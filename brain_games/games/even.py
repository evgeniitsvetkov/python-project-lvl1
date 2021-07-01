#!/usr/bin/env python
import random

import brain_games.games.flow as flow


task = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    min_num = 1
    max_num = 100
    number_to_guess = random.randint(min_num, max_num)
    return number_to_guess


def get_answer(question):
    if question % 2 == 0:
        return 'yes'
    else:
        return 'no'


def brain_even():
    flow.game_flow(task, get_question, get_answer)
