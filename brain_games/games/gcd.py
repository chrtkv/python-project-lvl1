import math
import random

RULES = 'Find the greatest common divisor of given numbers.'


def generate_round():
    m = random.randint(1, 100)
    n = random.randint(1, 100)
    question = f'{m} {n}'
    answer = math.gcd(m, n)
    return question, str(answer)
