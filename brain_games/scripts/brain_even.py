#!/usr/bin/env python
import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def main():
    name = welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    guesses_in_a_row = 3

    while guesses_in_a_row > 0:
        random_int = random.randint(1, 100)
        print(f'Question: {random_int}')

        user_input = prompt.string('Your answer: ')
        answers = ['yes', 'no']
        modulo = {'yes': 0, 'no': 1}
        if user_input in answers and random_int % 2 == modulo[user_input]:
            print('Correct!')
            guesses_in_a_row -= 1
            if guesses_in_a_row == 0:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{user_input}' is wrong answer ;(. "
                  f"Correct answer was '{answers[random_int % 2]}'.\n"
                  f"Let's try again, {name}!")
            break


if __name__ == '__main__':
    main()
