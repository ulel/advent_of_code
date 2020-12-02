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
