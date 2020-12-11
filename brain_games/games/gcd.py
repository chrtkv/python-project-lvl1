import random

rules = 'Find the greatest common divisor of given numbers.'


def gcd(m, n):
    divisor = n if m > n else m

    def find_gcd(m, n, divisor):
        if m % divisor == 0 and n % divisor == 0:
            return divisor
        else:
            return find_gcd(m, n, divisor - 1)

    return (find_gcd(m, n, divisor))


def gcd_game():
    m = random.randint(1, 100)
    n = random.randint(1, 100)
    question = f'{m} {n}'
    answer = gcd(m, n)
    return (question, str(answer))
