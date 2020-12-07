import prompt


def engine(rules, game, attempts=3):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(rules)
    for _i in range(attempts):
        question, correct_answer = game()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if correct_answer != answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
