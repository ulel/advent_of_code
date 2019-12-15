def _translate_instruction(instruction_string):
    directions = {
        "U": (0, 1),
        "D": (0, -1),
        "R": (1, 0),
        "L": (-1, 0),
    }

    direction = instruction_string[0]
    steps = int(instruction_string[1:])

    return (steps * directions[direction][0], steps * directions[direction][1])


def get_cable_instructions():
    cables = []
    with open("input", "r") as input_file:
        for line in input_file:
            cables.append(
                [_translate_instruction(instruction) for instruction in line.split(",")]
            )

    return cables
