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
    ops = ['+', '-', '*']
    op = random.choices(ops)[0]
    a = random_int()
    b = random_int()
    question = f'{a} {op} {b}'
    return question


def get_answer(question):
    answer = eval(question)
    return str(answer)


def main():
    name = welcome_user()

    print('What is the result of the expression?')

    guesses_in_a_row = 3

    while guesses_in_a_row > 0:
        question = get_question()
        print(f'Question: {question}')

        user_input = prompt.string('Your answer: ')
        answer = get_answer(question)
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
