"""
--- Day 3: Crossed Wires ---

The gravity assist was successful, and you're well on your way to the Venus
refuelling station. During the rush back on Earth, the fuel management system
wasn't completely installed, so that's next on the priority list.

Opening the front panel reveals a jumble of wires. Specifically, two wires are
connected to a central port and extend outward on a grid. You trace the path
each wire takes as it leaves the central port, one wire per line of text (your
puzzle input).

The wires twist and turn, but the two wires occasionally cross paths. To fix
the circuit, you need to find the intersection point closest to the central
port. Because the wires are on a grid, use the Manhattan distance for this
measurement. While the wires do technically cross right at the central port
where they both start, this point does not count, nor does a wire count as
crossing with itself.

For example, if the first wire's path is R8,U5,L5,D3, then starting from the
central port (o), it goes right 8, up 5, left 5, and finally down 3:

...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........

Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4,
and left 4:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........

These wires cross at two locations (marked X), but the lower-left one is closer
to the central port: its distance is 3 + 3 = 6.

Here are a few more examples:

    R75,D30,R83,U83,L12,D49,R71,U7,L72
    U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
    R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
    U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135

What is the Manhattan distance from the central port to the closest
intersection?

--- Part Two ---

It turns out that this circuit is very timing-sensitive; you actually need to
minimize the signal delay.

To do this, calculate the number of steps each wire takes to reach each
intersection; choose the intersection where the sum of both wires' steps is
lowest. If a wire visits a position on the grid multiple times, use the steps
value from the first time it visits that position when calculating the total
value of a specific intersection.

The number of steps a wire takes is the total number of grid squares the wire
has entered to get to that location, including the intersection being
considered. Again consider the example from above:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........

In the above example, the intersection closest to the central port is reached
after 8+5+5+2 = 20 steps by the first wire and 7+6+4+3 = 20 steps by the second
wire for a total of 20+20 = 40 steps.

However, the top-right intersection is better: the first wire takes only 8+5+2
= 15 and the second wire takes only 7+6+2 = 15, a total of 15+15 = 30 steps.

Here are the best steps for the extra examples from above:

    R75,D30,R83,U83,L12,D49,R71,U7,L72
    U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
    R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
    U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps

What is the fewest combined steps the wires must take to reach an intersection?
"""
from typing import Dict, Sequence, Tuple

import aoc_03_input


def trace_cable(
    cable_id: int,
    path: Sequence[Tuple[int, int]],
    tiles: Sequence[Tuple[int, int]] = None,
) -> Tuple[Dict[Tuple[int, int], int], Tuple[int, int], int]:
    if tiles is None:
        tiles = {}

    closest_cross = None
    closest_distance = 0
    steps = 0
    shortest_total = None

    current_tile = (0, 0)
    tiles[current_tile] = (cable_id, 0) if current_tile not in tiles else (-1, 0)

    for next_move in path:
        for tile in _get_tiles_in_path(current_tile, next_move):
            steps += 1
            if tile in tiles and tiles[tile][0] != cable_id:
                total_steps = steps + tiles[tile][1]
                if tiles[tile] != -1 and (
                    not shortest_total or total_steps < shortest_total
                ):
                    shortest_total = total_steps

                tiles[tile] = (-1, total_steps)
                distance_to_center = _manhattan_distance((0, 0), tile)

                if not closest_cross or distance_to_center < closest_distance:
                    closest_cross = tile
            else:
                tiles[tile] = (cable_id, steps)
            current_tile = tile

    return (closest_cross, tiles, shortest_total)


def _get_tiles_in_path(start: Tuple[int, int], move: Tuple[int, int]):
    if move[0]:
        for x in _get_range(start[0], move[0]):
            yield (x, start[1])
    else:
        for y in _get_range(start[1], move[1]):
            yield (start[0], y)


def _get_range(start: int, diff: int):
    if diff > 0:
        return range(start + 1, start + diff + 1)

    return range(start - 1, start + diff - 1, -1)


def _manhattan_distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> int:
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def main():
    tiles = {}
    cable_id = 0

    for cable in aoc_03_input.get_cable_instructions():
        (closest_cross, _, shortest_total) = trace_cable(cable_id, cable, tiles)
        cable_id += 1

    print(f"part 1: {_manhattan_distance((0, 0), closest_cross)}")
    print(f"part 2: {shortest_total}")


if __name__ == "__main__":
    main()
