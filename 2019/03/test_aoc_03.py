import copy

import pytest

import aoc_03


@pytest.mark.parametrize(
    "start, diff, expected_range",
    [
        (0, 3, [1, 2, 3]),
        (0, -3, [-1, -2, -3]),
        (10, 1, [11]),
        (10, -1, [9]),
        (-10, 2, [-9, -8]),
        (-10, -2, [-11, -12]),
    ],
)
def test_get_range(start, diff, expected_range):
    aoc_03._get_range(start, diff) == list(expected_range)


@pytest.mark.parametrize(
    "start, move, expected_coordinates",
    [
        pytest.param(
            (0, 0), (3, 0), [(1, 0), (2, 0), (3, 0)], id="from_center_x_positive"
        ),
        pytest.param(
            (0, 0), (0, 3), [(0, 1), (0, 2), (0, 3)], id="from_center_y_positive"
        ),
        pytest.param(
            (0, 0), (-3, 0), [(-1, 0), (-2, 0), (-3, 0)], id="from_center_x_negative"
        ),
        pytest.param(
            (0, 0), (0, -3), [(0, -1), (0, -2), (0, -3)], id="from_center_y_negative"
        ),
        pytest.param(
            (11, 21),
            (-5, 0),
            [(10, 21), (9, 21), (8, 21), (7, 21), (6, 21)],
            id="from_all_positive_x_negative",
        ),
        pytest.param(
            (11, 21),
            (0, -5),
            [(11, 20), (11, 19), (11, 18), (11, 17), (11, 16)],
            id="from_all_positive_y_negative",
        ),
        pytest.param(
            (11, 21), (2, 0), [(12, 21), (13, 21)], id="from_all_positive_x_positive"
        ),
        pytest.param(
            (11, 21), (0, 2), [(11, 22), (11, 23)], id="from_all_positive_y_positive"
        ),
    ],
)
def test_get_new_occupied_tiles(start, move, expected_coordinates):
    assert list(aoc_03._get_tiles_in_path(start, move)) == expected_coordinates


@pytest.mark.parametrize(
    "point1, point2, expected_distance",
    [
        ((0, 0), (0, 1), 1),
        ((0, 0), (1, 0), 1),
        ((0, 0), (-3, 0), 3),
        ((0, 0), (0, -2), 2),
        ((5, 3), (2, 1), 5),
    ],
)
def test_manhattan_distance(point1, point2, expected_distance):
    assert aoc_03._manhattan_distance(point1, point2) == expected_distance


def test_trace_cable_one_move():
    assert aoc_03.trace_cable(0, [(0, 3)], tiles={}) == (
        None,
        {(0, 0): (0, 0), (0, 1): (0, 1), (0, 2): (0, 2), (0, 3): (0, 3),},
        None,
    )


def test_trace_cable_multiple_moves():
    assert aoc_03.trace_cable(0, [(0, 3), (-2, 0)], tiles={}) == (
        None,
        {
            (0, 0): (0, 0),
            (0, 1): (0, 1),
            (0, 2): (0, 2),
            (0, 3): (0, 3),
            (-1, 3): (0, 4),
            (-2, 3): (0, 5),
        },
        None,
    )


def test_trace_cable_multiple_moves():
    orig_tiles = {
        (0, 0): (0, 0),
        (0, 1): (0, 1),
        (0, 2): (0, 2),
        (0, 3): (0, 3),
        (-1, 3): (0, 4),
        (-2, 3): (0, 5),
    }

    expected_tiles = copy.deepcopy(orig_tiles)
    expected_tiles[(0, 0)] = (-1, 0)
    expected_tiles[(-1, 0)] = (1, 1)
    expected_tiles[(-1, 1)] = (1, 2)
    expected_tiles[(0, 1)] = (-1, 4)
    expected_tiles[(1, 1)] = (1, 4)

    assert aoc_03.trace_cable(1, [(-1, 0), (0, 1), (2, 0)], tiles=orig_tiles) == (
        (0, 1),
        expected_tiles,
        4,
    )
