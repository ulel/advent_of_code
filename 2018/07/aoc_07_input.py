def get_input():
    """Return the input according to expected format of solver."""
    with open("input", "r") as input_file:
        for line in input_file:
            yield _parse_step(line)


def _parse_step(step_line):
    dependency = step_line[5]
    succeeding = step_line[36]
    return (dependency, succeeding)
