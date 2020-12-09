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
    first_argument = random.randint(0, 100)
    second_argument = random.randint(0, 100)
    question = f'{first_argument} {operator} {second_argument}'
    correct_answer = operators[operator](first_argument, second_argument)
    return (question, str(correct_answer))
