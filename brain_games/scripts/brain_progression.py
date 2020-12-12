#! /usr/bin/env python3
from brain_games.engine import engine
from brain_games.games.progression import progression_game, RULES


def main():
    engine(RULES, progression_game)


if __name__ == '__main__':
    main()
