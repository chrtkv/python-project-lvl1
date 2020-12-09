#! /usr/bin/env python3
from brain_games.cli import engine
from brain_games.games.calc import calc_game, rules


def main():
    engine(rules, calc_game)


if __name__ == '__main__':
    main()
