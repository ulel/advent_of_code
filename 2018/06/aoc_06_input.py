def get_input():
    """Return input as expected by Advent of Code 2018 day 6 solver."""
    with open("input", "r") as input_file:
        for input_line in input_file:
            coordinates = input_line.split(",")
            yield (int(coordinates[0]), int(coordinates[1]))
