#! /usr/bin/env python3
from brain_games.engine import engine
from brain_games.games.prime import prime_game, RULES


def main():
    engine(RULES, prime_game)


if __name__ == '__main__':
    main()
