/*
--- Day 2: Password Philosophy ---

Your flight departs in a few days from the coastal airport; the easiest way down to the coast from
here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with
our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been
allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according
to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy indicates the lowest
and highest number of times a given letter must appear for the password to be valid. For example,
1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no
instances of b, but needs at least 1. The first and third passwords are valid: they contain one a
or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

--- Part Two ---

While it appears you validated the passwords correctly, they don't seem to be what the Official
Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from
his old job at the sled rental place down the street! The Official Toboggan Corporate Policy
actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2
means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of
"index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of
the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?
*/

use std::fs::File;
use std::io::{self, BufRead};

struct Password {
    min: usize,
    max: usize,
    required_letter: char,
    password: String,
}

impl Password {
    fn new(min: usize, max: usize, required_letter: char, password: String) -> Self {
        Password {
            min,
            max,
            required_letter,
            password,
        }
    }
}

fn main() {
    input();
}

fn input() {
    let mut part_1 = 0;
    let mut part_2 = 0;

    let input_file = File::open("input").expect("input file not found");
    let file_reader = io::BufReader::new(input_file);
    let lines = file_reader.lines();
    for line in lines {
        let password = parse_password_line(line.unwrap());

        if password_pass_part_1(&password) {
            part_1 += 1;
        }

        if password_pass_part_2(&password) {
            part_2 += 1;
        }
    }

    println!("Part 1: {}", part_1);
    println!("Part 2: {}", part_2);
}

fn parse_password_line(password_line: String) -> Password {
    let split_password_line: Vec<&str> = password_line.split(['-', ' ', ':'].as_ref()).collect();

    let min = split_password_line[0].parse::<usize>().unwrap();
    let max = split_password_line[1].parse::<usize>().unwrap();

    let required_letter = split_password_line[2].chars().next().unwrap();
    let password = split_password_line[4].to_string();

    Password::new(min, max, required_letter, password)
}

fn password_pass_part_1(password: &Password) -> bool {
    let number_of_required_letter = password.password.matches(password.required_letter).count();

    password.min <= number_of_required_letter && number_of_required_letter <= password.max
}

fn password_pass_part_2(password: &Password) -> bool {
    let password_chars = password.password.chars();
    let char_vector: Vec<char> = password_chars.collect();
    let char_at_first_pos = char_vector[password.min - 1] == password.required_letter;
    let char_at_second_pos = char_vector[password.max - 1] == password.required_letter;

    if char_at_first_pos {
        return !char_at_second_pos;
    } else {
        return char_at_second_pos;
    }
}
