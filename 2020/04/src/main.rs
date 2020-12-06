/*
--- Day 4: Passport Processing ---

You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of
your passport. While these documents are extremely similar, North Pole Credentials aren't issued by
a country and therefore aren't actually valid documentation for travel in most of the world.

It seems like you're not the only one having problems, though; a very long line has formed for the
automatic passport scanners, and the delay could upset your travel itinerary.

Due to some questionable network security, you realize you might be able to solve both of these
problems at the same time.

The automatic passport scanners are slow because they're having trouble detecting which passports
have all required fields. The expected fields are as follows:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

Passport data is validated in batch files (your puzzle input). Each passport is represented as a
sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank
lines.

Here is an example batch file containing four passports:

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in

The first passport is valid - all eight fields are present. The second passport is invalid - it is
missing hgt (the Height field).

The third passport is interesting; the only missing field is cid, so it looks like data from North
Pole Credentials, not a passport at all! Surely, nobody would mind if you made the system
temporarily ignore missing cid fields. Treat this "passport" as valid.

The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other
field is not, so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the number of valid passports - those that have all required fields. Treat cid as optional.
In your batch file, how many passports are valid?

--- Part Two ---

The line is moving more quickly now, but you overhear airport security talking about how passports
with invalid data are getting through. Better add some data validation, quick!

You can continue to ignore the cid field, but each other field has strict rules about what values
are valid for automatic validation:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

Your job is to count the passports where all required fields are both present and valid according
to the above rules. Here are some example values:

byr valid:   2002
byr invalid: 2003

hgt valid:   60in
hgt valid:   190cm
hgt invalid: 190in
hgt invalid: 190

hcl valid:   #123abc
hcl invalid: #123abz
hcl invalid: 123abc

ecl valid:   brn
ecl invalid: wat

pid valid:   000000001
pid invalid: 0123456789

Here are some invalid passports:

eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

Here are some valid passports:

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719

Count the number of valid passports - those that have all required fields and valid values.
Continue to treat cid as optional. In your batch file, how many passports are valid?
*/

use regex::Regex;
use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};

fn main() {
    let batch_file = parse_batch_file();

    let mut valid_passports_part_1 = 0;
    let mut valid_passports_part_2 = 0;

    for line in batch_file {
        let (valid_part_1, valid_part_2) = is_valid_passport(line);
        if valid_part_1 {
            valid_passports_part_1 += 1;
            if valid_part_2 {
                valid_passports_part_2 += 1;
            }
        }
    }
    println!("Part 1: {}", valid_passports_part_1);
    println!("Part 2: {}", valid_passports_part_2);
}

fn is_valid_passport(line: HashMap<String, String>) -> (bool, bool) {
    /*
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    cid (Country ID) - ignored, missing or not.
    */
    let mut number_of_fields = 0;
    let mut have_cid = false;

    let mut valid_part_2 = true;

    for (key, value) in line {
        number_of_fields += 1;
        match key.as_ref() {
            "byr" => valid_part_2 = valid_part_2 && validate_year(&value, 1920, 2002),
            "iyr" => valid_part_2 = valid_part_2 && validate_year(&value, 2010, 2020),
            "eyr" => valid_part_2 = valid_part_2 && validate_year(&value, 2020, 2030),
            "hgt" => valid_part_2 = valid_part_2 && validate_height(&value),
            "ecl" => valid_part_2 = valid_part_2 && validate_eye_color(&value),
            "hcl" => valid_part_2 = valid_part_2 && validate_hair_color(&value),
            "pid" => valid_part_2 = valid_part_2 && validate_passport_id(&value),
            "cid" => have_cid = true,
            _ => return (false, false),
        }
    }

    let valid_part_1 = number_of_fields == 8 || (number_of_fields == 7 && !have_cid);

    (valid_part_1, valid_part_2)
}

fn validate_year(year: &String, min: u32, max: u32) -> bool {
    let year = year.parse::<u32>().expect("not a valid year");
    min <= year && year <= max
}

fn validate_height(height_line: &String) -> bool {
    /*
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    */
    let height_unit = &height_line[height_line.len() - 2..];
    let height_str = &height_line[..height_line.len() - 2];

    match height_str.parse::<u32>() {
        Ok(height) => match height_unit {
            "cm" => return 150 <= height && height <= 193,
            "in" => return 59 <= height && height <= 76,
            _ => return false,
        },
        Err(_) => return false,
    }
}

fn validate_eye_color(color: &String) -> bool {
    /*
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    */
    ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"].contains(&color.as_ref())
}

fn validate_hair_color(color: &String) -> bool {
    /*
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    */
    let color_re = Regex::new(r"^#[0-9a-f]{6}$").unwrap();

    color_re.is_match(color.trim())
}

fn validate_passport_id(passport_id: &String) -> bool {
    /*
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    */
    let passport_re = Regex::new(r"^[0-9]{9}$").unwrap();

    passport_re.is_match(passport_id.trim())
}

fn parse_batch_file() -> Vec<HashMap<String, String>> {
    let mut batch_file: Vec<HashMap<String, String>> = Vec::new();

    let input_file = File::open("input").expect("input file could not be opened");
    let file_reader = io::BufReader::new(input_file);
    let mut lines = file_reader.lines().peekable();

    let mut current_entry: HashMap<String, String> = HashMap::new();

    while let Some(line) = lines.next() {
        let line = line.unwrap();
        current_entry.extend(parse_fields(&line));

        if line.trim().is_empty() || !lines.peek().is_some() {
            batch_file.push(current_entry);
            current_entry = HashMap::new();
        }
    }

    batch_file
}

fn parse_fields(fields: &String) -> HashMap<String, String> {
    let mut batch_line: HashMap<String, String> = HashMap::new();
    for field in fields.split_whitespace() {
        let split_field: Vec<&str> = field.split(":").collect();
        batch_line.insert(split_field[0].to_string(), split_field[1].to_string());
    }
    batch_line
}
