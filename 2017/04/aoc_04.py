""" aoc_04.py

    Solution for Advent of Code 2017 day 04
"""

import aoc_04_input


def valid(password, check_anagram=False):
    ''' valid(password, sort=False)

        Check if a password is valid, that there are no repeated words.

        If check_anagram is True, check that no word is an anagram of any other
        as well.
    '''
    pass_list = password.split()

    if check_anagram:
        pass_list = list(map(lambda word: ''.join(sorted(list(word))),
                             pass_list))

    return len(pass_list) == len(set(pass_list))


def valid_part_2(password):
    ''' valid_part_2(password)

        Wrapper to add check_anagram=True to solve part 2 of day 4 of Advent of
        Code 2017.
    '''
    return valid(password, check_anagram=True)


def main():
    ''' main()

        Main function that use the input from Advent of Code and print the
        answer for day fourth problem.
    '''

    num_part1 = sum(map(valid, aoc_04_input.get_input()))
    num_part2 = sum(map(valid_part_2, aoc_04_input.get_input()))

    print('Part 1: {}'.format(num_part1))
    print('Part 2: {}'.format(num_part2))


if __name__ == '__main__':
    main()
