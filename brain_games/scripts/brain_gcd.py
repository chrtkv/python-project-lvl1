#! /usr/bin/env python3
from brain_games.engine import engine
from brain_games.games.gcd import gcd_game, RULES


def main():
    engine(RULES, gcd_game)


if __name__ == '__main__':
    main()
