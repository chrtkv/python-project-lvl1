#! /usr/bin/env python3

from brain_games.cli import engine
from brain_games.games.prime import prime_game, rules


def main():
    engine(rules, prime_game)


if __name__ == '__main__':
    main()
