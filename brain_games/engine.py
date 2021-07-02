#!/usr/bin/env python
import prompt

GUESSES_TO_WIN = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def play_game(task_description, get_task):
    name = welcome_user()

    print(task_description)

    guesses_in_a_row = 0
    while guesses_in_a_row < GUESSES_TO_WIN:
        question, answer = get_task()
        print(f'Question: {question}')

        user_input = prompt.string('Your answer: ')
        if user_input == answer:
            print('Correct!')
            guesses_in_a_row += 1
            if guesses_in_a_row == GUESSES_TO_WIN:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{user_input}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.\n"
                  f"Let's try again, {name}!")
            break
