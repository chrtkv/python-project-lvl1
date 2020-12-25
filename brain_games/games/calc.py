import random
import operator

DESCRIPTION = 'What is the result of the expression?'

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def generate_round():
    sign = random.choice(['+', '-', '*'])
    m = random.randint(0, 100)
    n = random.randint(0, 100)
    question = f'{m} {sign} {n}'
    answer = OPERATIONS[sign](m, n)
    return question, str(answer)
