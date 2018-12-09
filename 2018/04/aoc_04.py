"""
--- Day 4: Repose Record ---

You've sneaked into another supply closet - this time, it's across from the
prototype suit manufacturing lab. You need to sneak inside and fix the issues
with the suit, but there's a guard stationed outside the lab, so this is as
close as you can safely get.

As you search the closet for anything that might help, you discover that you're
not the first person to want to sneak in. Covering the walls, someone has spent
an hour starting every midnight for the past few months secretly observing this
guard post! They've been writing down the ID of the one guard on duty that
night - the Elves seem to have decided that one guard was enough for the
overnight shift - as well as when they fall asleep or wake up while at their
post (your puzzle input).

For example, consider the following records, which have already been organized
into chronological order:

[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up

Timestamps are written using year-month-day hour:minute format. The guard
falling asleep or waking up is always the one whose shift most recently
started. Because all asleep/awake times are during the midnight hour (00:00 -
00:59), only the minute portion (00 - 59) is relevant for those events.

Visually, these records show that the guards are asleep at these times:

Date   ID   Minute
            000000000011111111112222222222333333333344444444445555555555
            012345678901234567890123456789012345678901234567890123456789
11-01  #10  .....####################.....#########################.....
11-02  #99  ........................................##########..........
11-03  #10  ........................#####...............................
11-04  #99  ....................................##########..............
11-05  #99  .............................................##########.....

The columns are Date, which shows the month-day portion of the relevant day;
ID, which shows the guard on duty that day; and Minute, which shows the minutes
during which the guard was asleep within the midnight hour. (The Minute
column's header shows the minute's ten's digit in the first row and the one's
digit in the second row.) Awake is shown as ., and asleep is shown as #.

Note that guards count as asleep on the minute they fall asleep, and they count
as awake on the minute they wake up. For example, because Guard #10 wakes up at
00:25 on 1518-11-01, minute 25 is marked as awake.

If you can figure out the guard most likely to be asleep at a specific time,
you might be able to trick that guard into working tonight so you can have the
best chance of sneaking in. You have two strategies for choosing the best
guard/minute combination.

Strategy 1: Find the guard that has the most minutes asleep. What minute does
that guard spend asleep the most?

In the example above, Guard #10 spent the most minutes asleep, a total of 50
minutes (20+25+5), while Guard #99 only slept for a total of 30 minutes
(10+10+10). Guard #10 was asleep most during minute 24 (on two days, whereas
any other minute the guard was asleep was only seen on one day).

While this example listed the entries in chronological order, your entries are
in the order you found them. You'll need to organize them before they can be
analyzed.

What is the ID of the guard you chose multiplied by the minute you chose? (In
the above example, the answer would be 10 * 24 = 240.)


--- Part Two ---

Strategy 2: Of all guards, which guard is most frequently asleep on the same
    minute?

In the example above, Guard #99 spent minute 45 asleep more than any other
guard or minute - three times in total. (In all other cases, any guard spent
any minute asleep at most twice.)

What is the ID of the guard you chose multiplied by the minute you chose? (In
the above example, the answer would be 99 * 45 = 4455.)
"""
import collections

import aoc_04_input


def parse_writing(line):
    split_line = line.split()
    date = split_line[0].split("-")

    year = int(date[0][1:])
    month = int(date[1])
    day = int(date[2])

    time = split_line[1].split(":")
    hour = int(time[0])
    minute = int(time[1][:-1])

    if split_line[2] == "Guard":
        return (year, month, day, hour, minute, "start", int(split_line[3][1:]))
    else:
        action = "sleep" if split_line[-1] == "asleep" else "wake"
        return (year, month, day, hour, minute, action)


def parse_wall_writings(wall_writings):
    for writing in wall_writings:
        yield parse_writing(writing)


def calculate_sleep_patterns(wall_writings):
    sleep_patterns = collections.defaultdict(
        lambda: {"total": 0, "sleep_pattern": collections.defaultdict(lambda: 0)}
    )
    current_guard = None
    fall_asleep = None
    sleepiest = None

    for observation in sorted(parse_wall_writings(wall_writings)):
        if observation[5] == "start":
            current_guard = observation[6]
            fall_asleep = None
        else:
            if fall_asleep:
                wake_up = observation[4]

                new_total = (
                    sleep_patterns[current_guard]["total"] + wake_up - fall_asleep
                )
                sleep_patterns[current_guard]["total"] = new_total

                if not sleepiest:
                    sleepiest = current_guard
                elif new_total > sleep_patterns[sleepiest]["total"]:
                    sleepiest = current_guard

                sleep_patterns[current_guard][
                    "sleep_pattern"
                ] = number_of_nights_per_minute(
                    [(fall_asleep, wake_up)],
                    nights_per_minute=sleep_patterns[current_guard]["sleep_pattern"],
                )
                fall_asleep = None
            else:
                fall_asleep = observation[4]

    return {"sleepiest": sleepiest, "sleep_patterns": sleep_patterns}


def number_of_nights_per_minute(sleep_pattern, nights_per_minute=None):
    if not nights_per_minute:
        nights_per_minute = collections.defaultdict(lambda: 0)

    for (start, end) in sleep_pattern:
        for minute in range(start, end):
            nights_per_minute[minute] += 1

    return nights_per_minute


def get_most_frequent_minute(sleep_pattern):
    return max(sleep_pattern.items(), key=lambda minute: minute[1])


def strategy_1(sleep_patterns):
    sleepiest = sleep_patterns["sleepiest"]
    sleepiest_sleep_pattern = sleep_patterns["sleep_patterns"][sleepiest][
        "sleep_pattern"
    ]
    return get_most_frequent_minute(sleepiest_sleep_pattern)[0] * sleepiest


def strategy_2(sleep_patterns):
    most_predictable_guard = None
    most_predictable_minute = None
    most_predictable_frequency = 0

    for (guard, sleep_pattern) in sleep_patterns["sleep_patterns"].items():
        (minute, frequency) = get_most_frequent_minute(sleep_pattern["sleep_pattern"])
        if frequency > most_predictable_frequency:
            most_predictable_guard = guard
            most_predictable_minute = minute
            most_predictable_frequency = frequency

    return most_predictable_guard * most_predictable_minute


def main():
    sleep_patterns = calculate_sleep_patterns(aoc_04_input.get_input())
    part_1 = strategy_1(sleep_patterns)

    print(f"Advent of Code 2018 04 part 1: {part_1}")

    part_2 = strategy_2(sleep_patterns)
    print(f"Advent of Code 2018 04 part 2: {part_2}")


if __name__ == "__main__":
    main()
