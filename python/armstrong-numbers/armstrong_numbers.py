from functools import reduce


def is_armstrong_number(number: int) -> bool:
    numbers = sum([int(n) ** len(str(number)) for n in str(number)])
    return number == numbers
