import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_round():
    start = random.randint(1, 100)
    step = random.randint(2, 10)
    size = random.randint(5, 10)
    progression = list(range(start, start + step * size, step))

    omitted_number_index = random.randint(0, size - 1)
    answer = progression[omitted_number_index]
    question = ' '.join(['..' if i == answer else str(i) for i in progression])

    return question, str(answer)
