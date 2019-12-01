def get_input():
    with open("input", "r") as input_file:
        for mass in input_file:
            yield int(mass)

