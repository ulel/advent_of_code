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


def test_number_of_nights_per_minute(observations, no_nights_per_minute_guard_10):
    assert (
        aoc_04.number_of_nights_per_minute([(5, 25), (30, 55), (24, 29)])
        == no_nights_per_minute_guard_10
    )


@pytest.fixture
def no_nights_per_minute_guard_10():
    five_to_twentyfour = [(minute, 1) for minute in range(5, 24)]
    thirty_to_fiftyfive = [(minute, 1) for minute in range(30, 55)]
    twentyfour = [(24, 2)]
    twentyfive_to_twentynine = [(minute, 1) for minute in range(25, 29)]
    return dict(
        five_to_twentyfour + thirty_to_fiftyfive + twentyfour + twentyfive_to_twentynine
    )


@pytest.fixture
def no_nights_per_minute_guard_99():
    thirtysix_to_forty = [(minute, 1) for minute in range(36, 40)]
    forty_to_fortyfive = [(minute, 2) for minute in range(40, 45)]
    fortyfive = [(45, 3)]
    fortysix_to_fifty = [(minute, 2) for minute in range(46, 50)]
    fifty_to_fiftyfive = [(minute, 1) for minute in range(50, 55)]
    return dict(
        thirtysix_to_forty
        + forty_to_fortyfive
        + fortyfive
        + fortysix_to_fifty
        + fifty_to_fiftyfive
    )


@pytest.fixture
def observations(no_nights_per_minute_guard_10, no_nights_per_minute_guard_99):
    return {
        10: {"total": 50, "sleep_pattern": no_nights_per_minute_guard_10},
        99: {"total": 30, "sleep_pattern": no_nights_per_minute_guard_99},
    }


def test_calculate_sleep_patterns(wall_writings, observations):
    expected = {"sleepiest": 10, "sleep_patterns": observations}

    result = aoc_04.calculate_sleep_patterns(wall_writings)
    assert result == expected


def test_strategy_1(observations):
    assert aoc_04.strategy_1({"sleepiest": 10, "sleep_patterns": observations}) == 240


def test_strategy_1(observations):
    assert aoc_04.strategy_2({"sleepiest": 10, "sleep_patterns": observations}) == 4455
