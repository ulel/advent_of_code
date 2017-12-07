""" aoc_01.py

    Solution for Advent of Code 2017 day 01
"""


def solve_part_1(puzzle_input):
    ''' solve_part_1(puzzle_input)

        Calculate the solution to Advent of Code 2017 part 1.
    '''
    return calculate(puzzle_input)


def solve_part_2(puzzle_input):
    ''' solve_part_2(puzzle_input)

        Calculate the solution to Advent of Code 2017 part 2.
    '''
    return calculate(puzzle_input, len(puzzle_input) // 2)


def calculate(puzzle_input, offset=1):
    """ calculate(puzzle_input, offset)

        Calculate the answer to Advent of Code day 1.

        Default offset is 1, the setting for part 1.
    """

    length = len(puzzle_input)

    total = 0

    for i in range(0, length):
        current = puzzle_input[i]
        index = i + offset

        index = index - length if index >= length else index

        if current == puzzle_input[index]:
            total += int(current)

    return total


def main():
    ''' main()

        Print out the answer to Advent of Code 2017 day 1, both part 1 and 2.
    '''
    with open('input') as input_file:
        puzzle_input = input_file.readline().strip()

    print('Day 1 - Part 1: {}'.format(solve_part_1(puzzle_input)))
    print('Day 2 - Part 2: {}'.format(solve_part_2(puzzle_input)))


if __name__ == '__main__':
    main()
