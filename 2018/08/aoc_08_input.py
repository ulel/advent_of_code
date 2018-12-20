import re


def get_input():
    """Return the input as expected by solution for advent of code 2018 day 08."""
    with open("input", "r") as input_file:
        for line in input_file:
            return [int(number) for number in line.strip().split()]
