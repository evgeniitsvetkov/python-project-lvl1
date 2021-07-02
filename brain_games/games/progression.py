#!/usr/bin/env python
import random


START_MIN = 1
START_MAX = 19
STEP_MIN = 1
STEP_MAX = 9
LENGTH_MIN = 5
LENGTH_MAX = 10


task = 'What number is missing in the progression?'


def get_question():
    start = random.randint(START_MIN, STEP_MAX)
    step = random.randint(START_MIN, STEP_MAX)
    length = random.randint(LENGTH_MIN, LENGTH_MAX)
    end = start + (step * length)
    progression = [str(x) for x in range(start, end, step)]

    index_min = 1
    index_max = len(progression) - 2
    index = random.randint(index_min, index_max)
    progression[index] = '..'
    progression_to_guess = ' '.join(progression)
    return progression_to_guess


def get_answer(question):
    progression = question.split()
    i = progression.index('..')
    answer = str(int((int(progression[i - 1]) + int(progression[i + 1])) / 2))
    return answer
