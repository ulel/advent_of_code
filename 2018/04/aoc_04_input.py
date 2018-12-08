def get_input():
    """Return input as expected by the solver of Advent of Code day 4."""
    with open("input", "r") as input_file:
        for writing in input_file:
            yield writing
