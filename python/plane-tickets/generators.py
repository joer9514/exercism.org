"""Functions to automate Conda airlines ticketing system."""


from math import ceil
from typing import Generator


def generate_seat_letters(number: int) -> Generator[str, str, None]:
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    letters = "ABCD"
    for index in range(number):
        yield letters[index % len(letters)]


def generate_seats(number: int) -> Generator[str, str, None]:
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    letter = generate_seat_letters(number)
    for index in range(number):
        adjusted = ceil((index + 1) / 4)
        superstition = adjusted if adjusted < 13 else adjusted + 1

        yield f"{superstition}{next(letter)}"


def assign_seats(passengers: list[str]) -> dict[str, str]:
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    seats = generate_seats(len(passengers))
    return {passenger: seat for [passenger, seat] in zip(passengers, seats)}


def generate_codes(
    seat_numbers: list[str], flight_id: str
) -> Generator[str, str, None]:
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        unique_code = f"{seat}{flight_id}"

        difference = 12 - len(unique_code)
        unique_code += "0" * difference

        yield unique_code
