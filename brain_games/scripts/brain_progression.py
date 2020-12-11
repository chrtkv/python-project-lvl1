#! /usr/bin/env python3

from brain_games.cli import engine
from brain_games.games.progression import progression_game, rules


def main():
    engine(rules, progression_game)


if __name__ == '__main__':
    main()
