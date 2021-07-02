#!/usr/bin/env python
import random


START_MIN = 1
START_MAX = 19
STEP_MIN = 1
STEP_MAX = 9
LENGTH_MIN = 5
LENGTH_MAX = 10
INDEX_MIN = 0


task_description = 'What number is missing in the progression?'


def get_task():
    start = random.randint(START_MIN, START_MAX)
    step = random.randint(STEP_MIN, STEP_MAX)
    length = random.randint(LENGTH_MIN, LENGTH_MAX)
    end = start + (step * length)
    progression = [str(x) for x in range(start, end, step)]

    index = random.randint(INDEX_MIN, length - 1)
    answer = progression[index]
    progression[index] = '..'
    progression_to_guess = ' '.join(progression)
    return progression_to_guess, answer
