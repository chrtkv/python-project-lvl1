#! /usr/bin/env python3
from brain_games import games
from brain_games.engine import engine


def main():
    engine(games.prime)


if __name__ == '__main__':
    main()
