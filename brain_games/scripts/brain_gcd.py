#! /usr/bin/env python3

from brain_games.cli import engine
from brain_games.games.gcd import gcd_game, rules


def main():
    engine(rules, gcd_game)


if __name__ == '__main__':
    main()
