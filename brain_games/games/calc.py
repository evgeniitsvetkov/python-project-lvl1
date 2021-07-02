#!/usr/bin/env python
import random


MIN_NUM = 1
MAX_NUM = 100


task = 'What is the result of the expression?'


def get_question():
    a = random.randint(MIN_NUM, MAX_NUM)
    b = random.randint(MIN_NUM, MAX_NUM)
    ops = ['+', '-', '*']
    op = random.choice(ops)
    question = f'{a} {op} {b}'
    return question


def get_answer(question):
    answer = eval(question)
    return str(answer)
