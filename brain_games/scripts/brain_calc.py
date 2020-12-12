#! /usr/bin/env python3
from brain_games.engine import engine
from brain_games.games.calc import calc_game, RULES


def main():
    engine(RULES, calc_game)


if __name__ == '__main__':
    main()
