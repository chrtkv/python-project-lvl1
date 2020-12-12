#! /usr/bin/env python3
from brain_games.engine import engine
from brain_games.games.even import even_game, RULES


def main():
    engine(RULES, even_game)


if __name__ == '__main__':
    main()
