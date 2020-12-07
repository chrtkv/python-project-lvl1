import random


rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    return False


def even_game():
    question = random.randint(0, 100)
    correct_answer = 'yes' if is_even(question) else 'no'
    return (question, correct_answer)
