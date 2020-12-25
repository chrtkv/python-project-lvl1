import random
import operator

DESCRIPTION = 'What is the result of the expression?'

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def generate_round():
    operator = random.choice(['+', '-', '*'])
    m = random.randint(0, 100)
    n = random.randint(0, 100)
    question = f'{m} {operator} {n}'
    answer = OPERATORS[operator](m, n)
    return question, str(answer)
