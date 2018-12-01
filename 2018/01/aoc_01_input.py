"""
Format and return input for Advent of Code 2018 day 1.
"""


def get_input():
    """Yield an integer of each line of input."""
    with open("input", "r") as part_1_input:
        for change in part_1_input:
            yield (int(change))


def running_input():
    """Yield an integer of each line of input, start over when reaching the end of input."""
    while True:
        for change in get_input():
            yield change
