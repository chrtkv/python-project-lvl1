import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def engine(rules, game, attempts=3):
    name = welcome_user()

    print(rules)
    for _i in range(attempts):
        question, correct_answer = game()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if correct_answer != answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: E501
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
