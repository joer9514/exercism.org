from typing import Callable


def is_triangle(
    callback: Callable[[list[int | float]], bool]
) -> Callable[[list[int | float]], bool]:
    def valid_triangle(sides: list[int | float]) -> bool:
        return all(sides) and (sum(sides) >= max(sides) * 2) and callback(sides)

    return valid_triangle


@is_triangle
def equilateral(sides: list[int | float]) -> bool:
    return len(set(sides)) == 1


@is_triangle
def isosceles(sides: list[int | float]) -> bool:
    return len(set(sides)) < 3


@is_triangle
def scalene(sides: list[int | float]) -> bool:
    return len(set(sides)) == 3
