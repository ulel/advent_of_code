""" aoc_09.py

    Solution for Advent of Code 2017 day 09
"""

import aoc_09_input


def calculate_score(stream):
    ''' calculate_score(stream)

        Given a stream, calculate the score according to the rules from:
        http://adventofcode.com/2017/day/9
    '''

    nested = 0
    total = 0
    ignore = False
    garbage = False
    ignored_characters = 0

    for char in stream:
        if ignore:
            ignore = False
        elif char == '!':
            ignore = True
        elif garbage:
            if char == '>':
                garbage = False
            else:
                ignored_characters += 1
        elif char == '{':
            total += 1 + nested
            nested += 1
        elif char == '}':
            nested -= 1
        elif char == '<':
            garbage = True

    return total, ignored_characters


def main():
    ''' main()

        Main function that use the input from Advent of Code and print the
        answer to the problems for day nine.
    '''
    aoc_input = aoc_09_input.get_input()

    score, ignored = calculate_score(aoc_input)

    print('Part 1: {}'.format(score))
    print('Part 2: {}'.format(ignored))


if __name__ == '__main__':
    main()
