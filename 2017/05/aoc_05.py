""" aoc_05.py

    Solution for Advent of Code 2017 day 05
"""

import math

import aoc_05_input


def execute(instructions, dec_limit=math.inf):
    ''' execute(instructions)

        Executes the given list of instructions and print the number of steps
        it took to get out of the list.

        dec_limit is the limit for decreasing by 1 instead of incrementing,
        default is infinity.
    '''
    steps = 0
    index = 0

    while True:
        old_index = index
        try:
            index += instructions[index]
        except IndexError:
            return steps
        if instructions[old_index] >= dec_limit:
            instructions[old_index] -= 1
        else:
            instructions[old_index] += 1
        steps += 1


def main():
    ''' main()

        Main function that use the input from Advent of Code and print the
        answer for the problem for day five.
    '''
    aoc_input = aoc_05_input.get_input()

    print('Part 1: {}'.format(execute(aoc_input[:])))
    print('Part 2: {}'.format(execute(aoc_input[:], dec_limit=3)))


if __name__ == '__main__':
    main()
