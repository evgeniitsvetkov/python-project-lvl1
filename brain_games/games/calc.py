#!/usr/bin/env python
import random


MIN_NUM = 1
MAX_NUM = 100
OPS = ['+', '-', '*']
TASK_DESCRIPTION = 'What is the result of the expression?'


def get_task():
    a = random.randint(MIN_NUM, MAX_NUM)
    b = random.randint(MIN_NUM, MAX_NUM)
    op = random.choice(OPS)

    question = f'{a} {op} {b}'

    if op == '+':
        answer = a + b
    elif op == '-':
        answer = a - b
    elif op == '*':
        answer = a * b
    answer = str(answer)

    return question, answer
