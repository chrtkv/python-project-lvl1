import prompt
from brain_games.cli import welcome_user


def engine(game, attempts=3):
    name = welcome_user()
    print(game.RULES)
    for _ in range(attempts):
        question, correct_answer = game.generate_round()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if correct_answer != answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: E501
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
