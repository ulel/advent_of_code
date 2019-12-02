def get_instructions():
    with open("input", "r") as input_file:
        return [int(x) for x in input_file.read().split(",")]
