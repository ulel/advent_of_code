import aoc_02_input

def calculate_row(row):
    max_num = max(row)
    min_num = min(row)
    return max_num - min_num


def calculate_total(rows):
    return sum(map(calculate_row, rows))


def main():
    input_rows = aoc_02_input.get_input()

    print(calculate_total(input_rows))


if __name__ == '__main__':
    main()
