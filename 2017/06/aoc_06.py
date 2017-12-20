""" aoc_06.py

    Solution for Advent of Code 2017 day 06
"""

import aoc_06_input


def find_max(bank):
    ''' find_max(bank)

        Find the max number and its index in a list.
    '''
    max_index = -1
    current_max = -1

    for index in range(0, len(bank)):
        current = bank[index]

        if current > current_max:
            max_index = index
            current_max = current

    return (current_max, max_index)


def redistribute(value, index, bank):
    ''' redistribute(value, index, bank)

        Redistribute the value, sarting from index in the given memory bank.
    '''
    while value > 0:
        if index == len(bank):
            index = 0

        bank[index] += 1
        index += 1

        value -= 1

    return bank


def debug(bank, find_loop_length=False):
    ''' debug(bank, find_loop_length=False)

        Check how many cycles of redistribution it will take before ending up
        in the same state again.

        If find_loop_length is True it will instead return how long the loop
        between ending up in the same state twice after found it the first
        time.
    '''
    visited = dict()

    cycles = 0

    while tuple(bank) not in visited:
        visited[tuple(bank)] = True

        (value, index) = find_max(bank)

        cycles += 1

        bank[index] = 0

        redistribute(value, index+1, bank)

    if find_loop_length:
        return debug(bank)

    return cycles


def main():
    ''' main()

        Main function that use the input from Advent of Code and print the
        answer to the problems for day six.
    '''
    aoc_input = aoc_06_input.get_input()

    print('Part 1: {}'.format(debug(aoc_input[:])))
    print('Part 2: {}'.format(debug(aoc_input[:], find_loop_length=True)))


if __name__ == '__main__':
    main()
