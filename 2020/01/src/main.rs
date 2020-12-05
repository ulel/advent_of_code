/*
--- Day 1: Report Repair ---

After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

--- Part Two ---

The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
*/

use std::fs::File;
use std::io::{self, BufRead};
use std::vec;

fn main() -> std::io::Result<()> {
    let input_file = File::open("input")?;
    let mut entries = vec::Vec::new();

    for entry_line in io::BufReader::new(input_file).lines() {
        // let next_entry = entry_string.trim().parse::<i32>().unwrap();
        if let Ok(entry_string) = entry_line {
            let next_entry = entry_string.trim().parse::<i32>().unwrap();
            entries.push(next_entry);
        }
    }

    for first_candidate in 0..entries.len() {
        for second_candidate in first_candidate + 1..entries.len() {
            if entries[first_candidate] + entries[second_candidate] == 2020 {
                println!(
                    "1: {}",
                    entries[first_candidate] * entries[second_candidate]
                );
            }
        }
    }

    for first_candidate in 0..entries.len() {
        for second_candidate in first_candidate + 1..entries.len() {
            for third_candidate in second_candidate + 1..entries.len() {
                if entries[first_candidate] + entries[second_candidate] + entries[third_candidate]
                    == 2020
                {
                    println!(
                        "2: {}",
                        entries[first_candidate]
                            * entries[second_candidate]
                            * entries[third_candidate]
                    );
                }
            }
        }
    }

    Ok(())
}
