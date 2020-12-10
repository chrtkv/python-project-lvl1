import random
import operator


rules = 'What is the result of the expression?'


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def calc_game():
    operator = random.choice(['+', '-', '*'])
    m = random.randint(0, 100)
    n = random.randint(0, 100)
    question = f'{m} {operator} {n}'
    correct_answer = operators[operator](m, n)
    return (question, str(correct_answer))
