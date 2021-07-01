#!/usr/bin/env python
import random

import brain_games.games.flow as flow


task = 'What number is missing in the progression?'


def get_question():
    start_min = 1
    start_max = 19
    start = random.randint(start_min, start_max)

    step_min = 1
    step_max = 9
    step = random.randint(step_min, step_max)

    length_min = 5
    length_max = 10
    length = random.randint(length_min, length_max)

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


def brain_progression():
    flow.game_flow(task, get_question, get_answer)
