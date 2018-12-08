import textwrap

import pytest

import aoc_04


@pytest.mark.parametrize(
    "line, expected",
    [
        ("[1518-11-01 00:00] Guard #10 begins shift", (1518, 11, 1, 0, 0, "start", 10)),
        ("[1518-11-01 00:05] falls asleep", (1518, 11, 1, 0, 5, "sleep")),
        ("[1518-11-01 00:25] wakes up", (1518, 11, 1, 0, 25, "wake")),
    ],
)
def test_parse_writing(line, expected):
    assert aoc_04.parse_writing(line) == expected


@pytest.fixture
def wall_writings():
    return [
        "[1518-11-01 00:00] Guard #10 begins shift",
        "[1518-11-01 00:05] falls asleep",
        "[1518-11-01 00:25] wakes up",
        "[1518-11-01 00:30] falls asleep",
        "[1518-11-01 00:55] wakes up",
        "[1518-11-01 23:58] Guard #99 begins shift",
        "[1518-11-02 00:40] falls asleep",
        "[1518-11-02 00:50] wakes up",
        "[1518-11-03 00:05] Guard #10 begins shift",
        "[1518-11-03 00:24] falls asleep",
        "[1518-11-03 00:29] wakes up",
        "[1518-11-04 00:02] Guard #99 begins shift",
        "[1518-11-04 00:36] falls asleep",
        "[1518-11-04 00:46] wakes up",
        "[1518-11-05 00:03] Guard #99 begins shift",
        "[1518-11-05 00:45] falls asleep",
        "[1518-11-05 00:55] wakes up",
    ]


@pytest.fixture
def observations():
    return {
        10: {"total": 50, "sleep_pattern": [(5, 25), (30, 55), (24, 29)]},
        99: {"total": 30, "sleep_pattern": [(40, 50), (36, 46), (45, 55)]},
    }


def test_find_the_sleepiest(wall_writings, observations):
    assert aoc_04.find_the_sleepiest(wall_writings) == (10, observations[10])


def test_number_of_nights_per_minute(observations):
    five_to_twentyfour = [(minute, 1) for minute in range(5, 24)]
    thirty_to_fiftyfive = [(minute, 1) for minute in range(30, 55)]
    twentyfour = [(24, 2)]
    twentyfive_to_twentynine = [(minute, 1) for minute in range(25, 29)]
    expected = dict(
        five_to_twentyfour + thirty_to_fiftyfive + twentyfour + twentyfive_to_twentynine
    )
    assert (
        aoc_04.number_of_nights_per_minute(observations[10]["sleep_pattern"])
        == expected
    )


def test_strategy_1(observations):
    expected = 240

    assert aoc_04.strategy_1((10, observations[10])) == 240
