#!/usr/bin/env python
import random


MIN_NUM = 1
MAX_NUM = 100
OPERATOR_SIGNS = ['+', '-', '*']
TASK_DESCRIPTION = 'What is the result of the expression?'


def get_task():
    num_a = random.randint(MIN_NUM, MAX_NUM)
    num_b = random.randint(MIN_NUM, MAX_NUM)
    operator_sign = random.choice(OPERATOR_SIGNS)

    question = f'{num_a} {operator_sign} {num_b}'

    if operator_sign == '+':
        answer = num_a + num_b
    elif operator_sign == '-':
        answer = num_a - num_b
    elif operator_sign == '*':
        answer = num_a * num_b
    answer = str(answer)

    return question, answer
