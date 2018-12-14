"""
--- Day 6: Chronal Coordinates ---

The device on your wrist beeps several times, and once again you feel like
you're falling.

"Situation critical," the device announces. "Destination indeterminate. Chronal
interference detected. Please specify new target coordinates."

The device then produces a list of coordinates (your puzzle input). Are they
places it thinks are safe or dangerous? It recommends you check manual page
729. The Elves did not give you a manual.

If they're dangerous, maybe you can minimize the danger by finding the
coordinate that gives the largest distance from the other points.

Using only the Manhattan distance, determine the area around each coordinate by
counting the number of integer X,Y locations that are closest to that
coordinate (and aren't tied in distance to any other coordinate).

Your goal is to find the size of the largest area that isn't infinite. For
example, consider the following list of coordinates:

1, 1
1, 6
8, 3
3, 4
5, 5
8, 9

If we name these coordinates A through F, we can draw them on a grid, putting
0,0 at the top left:

..........
.A........
..........
........C.
...D......
.....E....
.B........
..........
..........
........F.

This view is partial - the actual grid extends infinitely in all directions.
Using the Manhattan distance, each location's closest coordinate can be
determined, shown here in lowercase:

aaaaa.cccc
aAaaa.cccc
aaaddecccc
aadddeccCc
..dDdeeccc
bb.deEeecc
bBb.eeee..
bbb.eeefff
bbb.eeffff
bbb.ffffFf

Locations shown as . are equally far from two or more coordinates, and so they
don't count as being closest to any.

In this example, the areas of coordinates A, B, C, and F are infinite - while
not shown here, their areas extend forever outside the visible grid. However,
the areas of coordinates D and E are finite: D is closest to 9 locations, and E
is closest to 17 (both including the coordinate's location itself). Therefore,
in this example, the size of the largest area is 17.

What is the size of the largest area that isn't infinite?
"""
import collections
import math

import aoc_06_input


def max_x_and_y(locations):
    max_x = -1
    max_y = -1

    for (x, y) in locations:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    return (max_x, max_y)


def manhattan_distance(location_1, location_2):
    return abs((location_1[0] - location_2[0])) + abs((location_1[1] - location_2[1]))


def generate_grid(locations):
    (max_x, max_y) = max_x_and_y(locations)
    grid = dict()
    border_locations = set()

    for column in range(0, max_x + 2):
        for row in range(0, max_y + 2):
            closest = closest_location((column, row), locations)
            grid[(column, row)] = closest
            if column == 0 or column > max_x:
                border_locations.add(closest)
            if row == 0 or row > max_y:
                border_locations.add(closest)

    return (grid, border_locations)


def closest_location(point, locations):
    closest_distance = math.inf
    closest_location = None

    for location in locations:
        distance = manhattan_distance(point, location)
        if distance < closest_distance:
            closest_location = location
            closest_distance = distance
        elif distance == closest_distance:
            closest_location = None

    return closest_location


def find_largest_area(grid, border_locations):
    areas = collections.defaultdict(lambda: 0)

    for (position, location) in grid.items():
        if location and location not in border_locations:
            areas[location] += 1

    return areas[max(areas, key=areas.get)]


def size_of_largest_area(locations):
    (grid, border_locations) = generate_grid(locations)
    largest_area = find_largest_area(grid, border_locations)

    return largest_area


def main():
    part_1 = size_of_largest_area(list(aoc_06_input.get_input()))

    print(f"Advent of Code 2018 day 6 part 1: {part_1}")


if __name__ == "__main__":
    main()
