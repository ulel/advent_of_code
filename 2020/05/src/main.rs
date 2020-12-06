/*
--- Day 5: Binary Boarding ---

You board your plane only to discover a new problem: you dropped your boarding pass! You aren't
sure which seat is yours, and all of the flight attendants are busy with the flood of people that
suddenly made it through passport control.

You write a quick program to use your phone's camera to scan all of the nearby boarding passes
(your puzzle input); perhaps you can find your seat through process of elimination.

Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat
might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R
means "right".

The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the
plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in.
Start with the whole list of rows; the first letter indicates whether the seat is in the front (0
through 63) or the back (64 through 127). The next letter indicates which half of that region the
seat is in, and so on until you're left with exactly one row.

For example, consider just the first seven characters of FBFBBFFRLR:

    Start by considering the whole range, rows 0 through 127.
    F means to take the lower half, keeping rows 0 through 63.
    B means to take the upper half, keeping rows 32 through 63.
    F means to take the lower half, keeping rows 32 through 47.
    B means to take the upper half, keeping rows 40 through 47.
    B keeps rows 44 through 47.
    F keeps rows 44 through 45.
    The final F keeps the lower of the two, row 44.

The last three characters will be either L or R; these specify exactly one of the 8 columns of
seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with
only three steps. L means to keep the lower half, while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

    Start by considering the whole range, columns 0 through 7.
    R means to take the upper half, keeping columns 4 through 7.
    L means to take the lower half, keeping columns 4 through 5.
    The final R keeps the upper of the two, column 5.

So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example,
the seat has ID 44 * 8 + 5 = 357.

Here are some other boarding passes:

    BFFFBBFRRR: row 70, column 7, seat ID 567.
    FFFBBBFRRR: row 14, column 7, seat ID 119.
    BBFFBBFRLL: row 102, column 4, seat ID 820.

As a sanity check, look through your list of boarding passes. What is the highest seat ID on a
boarding pass?

--- Part Two ---

Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding pass in your list.
However, there's a catch: some of the seats at the very front and back of the plane don't exist on
this aircraft, so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be
in your list.

What is the ID of your seat?
*/

use std::fs::File;
use std::io::{self, BufRead};

fn main() {
    println!("Hello, world!");
    let mut seat_ids = get_seat_ids();

    println!("Part 1: {}", seat_ids.iter().max().unwrap());

    seat_ids.sort_unstable();

    let mut skip = true;

    let mut last_seat = 0;

    for seat in seat_ids {
        if skip {
            last_seat = seat;
            skip = false;
            continue;
        }
        if last_seat + 1 != seat {
            println!("Part 2: {}", seat - 1);
            break;
        }
        last_seat = seat;
    }
}

fn get_seat_ids() -> Vec<u32> {
    let mut seat_ids: Vec<u32> = Vec::new();

    let input_file = File::open("input").expect("input file could not be opened");
    let file_reader = io::BufReader::new(input_file);
    let lines = file_reader.lines();

    for line in lines {
        let line = line.unwrap();

        let row_code = &line[..7];
        let column_code = &line[7..];
        let row = decode_row(row_code);
        let column = decode_column(column_code);

        seat_ids.push(row * 8 + column);
    }

    seat_ids
}

fn decode_row(row_code: &str) -> u32 {
    let mut current_low = 0;
    let mut current_high = 128;

    for code in row_code.chars() {
        match code {
            'F' => current_high = current_low + ((current_high - current_low) / 2),
            'B' => current_low = current_high - ((current_high - current_low) / 2),
            _ => panic!("unknown code in row_code"),
        }
    }

    current_high - 1
}

fn decode_column(column_code: &str) -> u32 {
    let mut current_high = 8;
    let mut current_low = 0;

    for code in column_code.chars() {
        match code {
            'L' => current_high = current_low + ((current_high - current_low) / 2),
            'R' => current_low = current_high - ((current_high - current_low) / 2),
            _ => panic!("unknown code in column_code"),
        }
    }

    current_high - 1
}

#[cfg(test)]
mod tests {
    /*
    For example, consider just the first seven characters of FBFBBFFRLR:

    Start by considering the whole range, rows 0 through 127.
    F means to take the lower half, keeping rows 0 through 63.
    B means to take the upper half, keeping rows 32 through 63.
    F means to take the lower half, keeping rows 32 through 47.
    B means to take the upper half, keeping rows 40 through 47.
    B keeps rows 44 through 47.
    F keeps rows 44 through 45.
    The final F keeps the lower of the two, row 44.

    BFFFBBFRRR: row 70, column 7, seat ID 567.
    FFFBBBFRRR: row 14, column 7, seat ID 119.
    BBFFBBFRLL: row 102, column 4, seat ID 820.
    */
    use super::*;

    #[test]
    fn test_decode_row_44() {
        assert_eq!(decode_row("FBFBBFF"), 44);
    }

    #[test]
    fn test_decode_row_70() {
        assert_eq!(decode_row("BFFFBBF"), 70);
    }

    #[test]
    fn test_decode_row_14() {
        assert_eq!(decode_row("FFFBBBF"), 14);
    }

    #[test]
    fn test_decode_row_102() {
        assert_eq!(decode_row("BBFFBBF"), 102);
    }

    #[test]
    fn test_decode_column_5() {
        assert_eq!(decode_column("RLR"), 5);
    }

    #[test]
    fn test_decode_column_7() {
        assert_eq!(decode_column("RRR"), 7);
    }

    #[test]
    fn test_decode_column_4() {
        assert_eq!(decode_column("RLL"), 4);
    }
}
