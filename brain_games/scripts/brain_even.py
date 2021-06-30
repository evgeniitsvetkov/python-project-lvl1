#!/usr/bin/env python
import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def random_int(start=1, end=100):
    return random.randint(start, end)


def get_question():
	number_to_guess = random_int()
	return number_to_guess


def get_answer(question, user_input):
    answers = ['yes', 'no']
    if user_input not in answers or question % 2 == 1:
        return 'no'
    else:
        return 'yes'


def main():
    name = welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    guesses_in_a_row = 3

    while guesses_in_a_row > 0:
        question = get_question()
        print(f'Question: {question}')

        user_input = prompt.string('Your answer: ')
        answer = get_answer(question, user_input)
        if user_input == answer:
            print('Correct!')
            guesses_in_a_row -= 1
            if guesses_in_a_row == 0:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{user_input}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.\n"
                  f"Let's try again, {name}!")
            break


if __name__ == '__main__':
    main()
