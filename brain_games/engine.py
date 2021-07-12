#!/usr/bin/env python
import prompt

GUESSES_TO_WIN = 3


def play_game(task_description, get_task):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n{task_description}')

    tries = GUESSES_TO_WIN
    while tries:
        question, task_answer = get_task()
        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')
        if user_answer == task_answer:
            print('Correct!')
            tries -= 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{task_answer}'.\n"
                  f"Let's try again, {name}!")
            break

    else:
        print(f'Congratulations, {name}!')
