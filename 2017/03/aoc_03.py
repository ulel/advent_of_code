""" aoc_03.py

    Solution for Advent of Code 2017 day 03
"""

import aoc_03_input


def layer_size(layer):
    ''' layer_size(layer)

        Return the size of a layer.
    '''

    if layer == 0:
        return 1

    return (layer*2-1)*4+4


def layer_no(square):
    ''' layer_no(square)

        Return the layer a square belongs to and the last number of that layer.
    '''
    layer = 0
    total = 0

    while True:
        size = layer_size(layer)
        total += size
        if square <= total:
            return (layer, size, total)
        layer += 1


def cord(square):
    ''' cord(square)

        Return the coordinate of a given square.
    '''
    (x_cord, size, last_square) = layer_no(square)

    max_cord = (size//4+1)//2

    coordinates = list(range(max_cord, 0-max_cord, -1))*4

    y_cord = 0 if square == 1 else coordinates[last_square-square]

    return (x_cord, y_cord)


def distance(square):
    ''' calculate_distance(square)

        Calculates the number of steps a square has to travel to reach 1.
    '''
    (x_cord, y_cord) = cord(square)

    return x_cord + abs(y_cord)


def main():
    ''' main()

        Main function that use the input from Advent of Code and print the
        answer for day threes problem.
    '''
    print(distance(aoc_03_input.get_input()))


if __name__ == '__main__':
    main()
