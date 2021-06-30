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
    start = random_int(1, 20)
    step = random_int(2, 9)
    length = random_int(5, 10)
    end = start + (step * length)
    progression = [str(x) for x in range(start, end, step)]

    i = random_int(1, len(progression) - 2)
    progression[i] = '..'
    progression_to_guess = ' '.join(progression)
    return progression_to_guess


def get_answer(question):
    progression = question.split()
    i = progression.index('..')
    answer = str(int((int(progression[i - 1]) + int(progression[i + 1])) / 2))
    return answer


def main():
    name = welcome_user()

    print('Find the greatest common divisor of given numbers.')

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
