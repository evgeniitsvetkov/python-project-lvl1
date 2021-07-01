#!/usr/bin/env python
import random

import brain_games.games.flow as flow


task = 'What is the result of the expression?'


def get_question():
    min_num = 1
    max_num = 50
    a = random.randint(min_num, max_num)
    b = random.randint(min_num, max_num)
    ops = ['+', '-', '*']
    op = random.choices(ops)[0]
    question = f'{a} {op} {b}'
    return question


def get_answer(question):
    answer = eval(question)
    return str(answer)


def brain_calc():
    flow.game_flow(task, get_question, get_answer)
