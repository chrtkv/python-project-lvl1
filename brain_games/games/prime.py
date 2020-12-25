import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n < 2:
        return False

    divisor = n // 2

    def inner(n, divisor):
        if divisor == 1:
            return True
        if n % divisor == 0:
            return False
        return inner(n, divisor - 1)

    return inner(n, divisor)


def generate_round():
    question = random.randint(0, 500)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
