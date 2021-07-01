#!/usr/bin/env python
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_flow(task, get_question, get_answer):
    name = welcome_user()

    print(task)

    guesses_in_a_row = 0
    while guesses_in_a_row < 3:
        question = get_question()
        print(f'Question: {question}')

        user_input = prompt.string('Your answer: ')
        answer = get_answer(question)
        if user_input == answer:
            print('Correct!')
            guesses_in_a_row += 1
            if guesses_in_a_row == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{user_input}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.\n"
                  f"Let's try again, {name}!")
            break
