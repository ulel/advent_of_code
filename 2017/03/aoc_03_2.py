""" aoc_03_2.py

    Solution for Advent of Code 2017 day 03 part 2
"""

import itertools

import aoc_03_input


def get_square(num):
    ''' get_square(num)

        Return the numth square in the spiral.
    '''
    return list(generate_spiral(num))[num-1]


def generate_spiral(max_square):
    ''' spiral(max_square)

        A generator that generates a spiral according to Advent of Code 2017,
        day 03 part 2.
    '''

    spiral = {}

    current_dir = (0, 1)
    cord = (0, 0)

    for i in range(0, max_square):
        if i > max_square:
            break

        spiral[cord] = value(cord, spiral)
        yield {'cord': cord, 'value': spiral[cord]}

        current_dir = get_direction(cord, current_dir, spiral)
        cord = (cord[0] + current_dir[0], cord[1] + current_dir[1])


def get_direction(cord, current_direction, spiral):
    ''' get_direction(cord, current_direction, spiral)

        Given a cordinate and the current_direction, it checks whatever turning
        now would end up in a non occupied square, if so, return the new
        direction, otherwise we keep going in the same direction.
    '''

    new_direction = next_direction(current_direction)

    check_cord = (cord[0] + new_direction[0],
                  cord[1] + new_direction[1])

    if spiral.get(check_cord):
        return current_direction

    return new_direction


def next_direction(direction):
    ''' next_direction(direction)

        Maps a given direction to a new direction so that we turn left all the
        time in the spiral.
    '''
    direction_mappings = {
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0),
        (-1, 0): (0, 1)
    }
    return direction_mappings[direction]


def value(cord, spiral):
    ''' value(cord, spiral)

        Get all values from neighbouring squares, and sums them up which is the
        value the square at cord should have.
    '''
    if cord == (0, 0):
        return 1

    neightbours_offsets = list(itertools.product([1, 0, -1], [1, 0, -1]))
    neightbours_offsets.remove((0, 0))  # Not interested in ourself

    neighbour_values = map(lambda offset: spiral.get((cord[0] + offset[0],
                                                      cord[1] + offset[1]), 0),
                           neightbours_offsets)
    return sum(neighbour_values)


def main():
    ''' main()

        Main function that use the input from Advent of Code and print the
        answer for day threes problem.
    '''
    target = aoc_03_input.get_input()

    # The square we want will always be in a square earlier than the target
    # value
    for square in generate_spiral(target):
        if square['value'] > target:
            print(square['value'])
            break


if __name__ == '__main__':
    main()
