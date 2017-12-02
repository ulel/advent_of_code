import aoc_02_input


def calculate_row(row):
    for i in range(len(row)):
        for j in range(i+1, len(row)):
            if row[i] > row[j]:
                if row[i] % row[j] == 0:
                    return row[i] // row[j]
            else:
                if row[j] % row[i] == 0:
                    return row[j] // row[i]


def calculate_total(rows):
    return sum(map(calculate_row, rows))


def main():
    input_rows = aoc_02_input.get_input()

    print(calculate_total(input_rows))


if __name__ == '__main__':
    main()
