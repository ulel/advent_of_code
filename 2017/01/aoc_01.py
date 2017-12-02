def solve_part_1(puzzle_input):
    first = puzzle_input[1]
    current = ''

    total = 0

    for i in puzzle_input:
        if i == current:
            total += int(i)
        current = i

    if current == first:
        total += int(current)

    return total


def solve_part_2(puzzle_input):
    length = len(puzzle_input)
    half = int(length/2)

    total = 0
    comparision = 0

    for i in range(0, len(puzzle_input)):
        current = puzzle_input[i]

        if (i + half) >= length:
            comparision = puzzle_input[ i+half-length ]
        else:
            comparision = puzzle_input[ i+half ]

        if current == comparision:
            total += int(current)

    return total


def main():
    with open('input') as input_file:
        puzzle_input = input_file.readline().strip()

    print('Day 1 - Part 1:')
    print(solve_part_1(puzzle_input))
    print('')
    print('Day 2 - Part 2:')
    print(solve_part_2(puzzle_input))


if __name__ == '__main__':
    main()
