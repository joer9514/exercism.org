def leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
