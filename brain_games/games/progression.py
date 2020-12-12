import random


rules = 'What number is missing in the progression?'


def progression_game():
    start = random.randint(1, 100)
    step = random.randint(2, 10)
    # size of progression — from 5 to 10 numbers
    size = random.choice(range(5, 11))
    progression = list(range(start, start + step * size, step))

    omitted_number_index = random.choice(range(0, size))
    answer = progression[omitted_number_index]
    question = ' '.join(['..' if i == answer else str(i) for i in progression])

    return(question, str(answer))
