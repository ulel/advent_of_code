// 54845
// --- Day 1: Trebuchet?! ---
//
// Something is wrong with global snow production, and you've been selected to take a look. The
// Elves have even given you a map; on it, they've used stars to mark the top fifty locations that
// are likely to be having problems.
//
// You've been doing this long enough to know that to restore snow operations, you need to check
// all fifty stars by December 25th.
//
// Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent
// calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one
// star. Good luck!
//
// You try to ask why they can't just use a weather machine ("not powerful enough") and where
// they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of
// questions") and hang on did you just say the sky ("of course, where do you think snow comes
// from") when you realize that the Elves are already loading you into a trebuchet ("please hold
// still, we need to strap you in").
//
// As they're making the final adjustments, they discover that their calibration document (your
// puzzle input) has been amended by a very young Elf who was apparently just excited to show off
// her art skills. Consequently, the Elves are having trouble reading the values on the document.
//
// The newly-improved calibration document consists of lines of text; each line originally
// contained a specific calibration value that the Elves now need to recover. On each line, the
// calibration value can be found by combining the first digit and the last digit (in that order)
// to form a single two-digit number.
//
// For example:
//
// 1abc2
// pqr3stu8vwx
// a1b2c3d4e5f
// treb7uchet
//
// In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these
// together produces 142.
//
// Consider your entire calibration document. What is the sum of all of the calibration values?
//

// --- Part Two ---
//
// Your calculation isn't quite right. It looks like some of the digits are actually spelled out
// with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid
// "digits".
//
// Equipped with this new information, you now need to find the real first and last digit on each
// line. For example:
//
// two1nine eightwothree abcone2threexyz xtwone3four 4nineeightseven2 zoneight234 7pqrstsixteen
//
// In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these
// together produces 281.
//
// What is the sum of all of the calibration values?

fn main() {
    let input = include_str!("../input");

    println!("Part 2: {}", part_2(input));
}

// part_1 need to ignore text numbers
fn part_2(input: &str) -> u32 {
    let mut total: u32 = 0;
    for line in input.lines() {
        total += extract_number(line);
    }
    total
}

fn potential_number(current: &str) -> (bool, Option<char>) {
    let numbers = vec![
        ("one", '1'),
        ("two", '2'),
        ("three", '3'),
        ("four", '4'),
        ("five", '5'),
        ("six", '6'),
        ("seven", '7'),
        ("eight", '8'),
        ("nine", '9'),
    ];

    for number in numbers {
        let (num_str, value) = number;
        if num_str.starts_with(current) {
            if num_str.len() == current.len() {
                return (true, Some(value));
            } else {
                return (true, None);
            }
        }
    }

    (false, None)
}

fn extract_number(line: &str) -> u32 {
    let mut first: char = '0';
    let mut last: char = '0';
    let mut found_first: bool = false;
    let mut potential: String = "".to_string();

    for character in line.chars() {
        potential = format!("{}{}", potential, character);
        let (could_be_text_number, value) = potential_number(&potential);

        if could_be_text_number {
            if value.is_some() {
                if !found_first {
                    first = value.unwrap();
                    found_first = true;
                }
                potential = character.to_string();
                last = value.unwrap();
            }
        } else {
            if potential.len() > 1 {
                potential = (potential[1..potential.len() - 1]).to_string();
                potential = format!("{}{}", potential, character.to_string());
            }
            if character.is_numeric() {
                potential = "".to_string();
                if !found_first {
                    first = character;
                    found_first = true;
                }
                last = character;
            }
        }
    }

    let complete_number = format!("{}{}", first, last);

    complete_number.parse::<u32>().unwrap()
}

#[cfg(test)]
mod tests {
    use super::*;

    macro_rules! extract_number_tests {
        ($($test_name:ident: $value:expr,)*) => {
        $(
            #[test]
            fn $test_name() {
                let (input, expected) = $value;
                assert_eq!(expected, extract_number(input));
            }
        )*
        }
    }

    extract_number_tests! {
        extract_number_1abc2: ("1abc2", 12),
        extract_number_pqr3stu8vwx: ("pqr3stu8vwx", 38),
        extract_number_a1b2c3d4e5f: ("a1b2c3d4e5f", 15),
        extract_number_treb7uchet: ("treb7uchet", 77),
        extract_number_two1nine: ("two1nine", 29),
        extract_number_eightwothree: ("eightwothree", 83),
        extract_number_abcone2threexyz: ("abcone2threexyz", 13),
        extract_number_xtwone3four: ("xtwone3four", 24),
        extract_number_4nineeightseven2: ("4nineeightseven2", 42),
        extract_number_zoneight234: ("zoneight234", 14),
        extract_number_7pqrstsixteen: ("7pqrstsixteen", 76),
        extract_number_eightwo: ("eightwo", 82),
        extract_number_eighteightwo: ("eighteightwo", 82),
        extract_number_six1mpffbnbnnlxthree: ("six1mpffbnbnnlxthree", 63),
        extract_number_4eight3one92: ("4eight3one92", 42),
        extract_number_qvcxfrjgm6threetwoeighttwoneg: ("qvcxfrjgm6threetwoeighttwoneg", 61),
        extract_number_eighthree: ("eighthree", 83),
        extract_number_sevenine: ("sevenine", 79),
        extract_number_nkkxzlrkgfonesevenfour7twompjpqdsvpp: ("nkkxzlrkgfonesevenfour7twompjpqdsvpp", 12),
        extract_number_xfoneight8sevenone3: ("xfoneight8sevenone3", 13),
        extract_number_threefrdlbmnqrreight4psfonegggjj: ("threefrdlbmnqrreight4psfonegggjj", 31),
        etxract_number_hffoneight96vqkbsgpzvn3sixtxh4ckjlm3: ("hffoneight96vqkbsgpzvn3sixtxh4ckjlm3", 13),
        extract_number_3twonine: ("3twonine", 39),
    }

    #[test]
    fn test_part_1() {
        let input = "1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet";

        assert_eq!(142, part_2(input));
    }

    #[test]
    fn test_part_2() {
        let input = "two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
";
        assert_eq!(281, part_2(input));
    }

    macro_rules! potential_number_tests {
        ($($test_name:ident: $value:expr,)*) => {
        $(
            #[test]
            fn $test_name() {
                let (current, expected) = $value;
                assert_eq!(expected, potential_number(current));
            }
        )*
        }
    }

    potential_number_tests! {
        potential_number_x: ("x", (false, None)),
        potential_number_o: ("o", (true, None)),
        potential_number_on: ("on", (true, None)),
        potential_number_one: ("one", (true, Some('1'))),
        potential_number_oc: ("oc", (false, None)),
        potential_number_onf: ("onf", (false, None)),
        potential_number_nine: ("nine", (true, Some('9'))),
        potential_number_five: ("five", (true, Some('5'))),
    }
}
