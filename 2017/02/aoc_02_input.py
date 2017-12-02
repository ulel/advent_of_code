def get_input():
    input_rows = []
    with open('input') as input_file:
        for line in input_file:
            row = list(map(int, line.split()))
            input_rows.append(row)

    return input_rows

