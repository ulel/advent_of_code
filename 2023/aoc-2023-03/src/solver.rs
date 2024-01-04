// --- Day 3: Gear Ratios ---
//
// You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you
// up to the water source, but this is as far as he can bring you. You go inside.
//
// It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.
//
// "Aaah!"
//
// You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I
// wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before
// I can fix it." You offer to help.
//
// The engineer explains that an engine part seems to be missing from the engine, but nobody can
// figure out which one. If you can add up all the part numbers in the engine schematic, it should
// be easy to work out which part is missing.
//
// The engine schematic (your puzzle input) consists of a visual representation of the engine.
// There are lots of numbers and symbols you don't really understand, but apparently any number
// adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum.
// (Periods (.) do not count as a symbol.)
//
// Here is an example engine schematic:
//
// 467..114..
// ...*......
// ..35..633.
// ......#...
// 617*......
// .....+.58.
// ..592.....
// ......755.
// ...$.*....
// .664.598..
//
// In this schematic, two numbers are not part numbers because they are not adjacent to a symbol:
// 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a
// part number; their sum is 4361.
//
// Of course, the actual engine schematic is much larger. What is the sum of all of the part
// numbers in the engine schematic?

// --- Part Two ---

// The engineer finds the missing part and installs it in the engine! As the engine springs to
// life, you jump in the closest gondola, finally ready to ascend to the water source.
//
// You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the
// gondola has a phone labeled "help", so you pick it up and the engineer answers.
//
// Before you can explain the situation, she suggests that you look out the window. There stands
// the engineer, holding a phone in one hand and waving with the other. You're going so slowly that
// you haven't even left the station. You exit the gondola.
//
// The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any
// * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of
// multiplying those two numbers together.
//
// This time, you need to find the gear ratio of every gear and add them all up so that the
// engineer can figure out which gear needs to be replaced.
//
// Consider the same engine schematic again:
//
// 467..114..
// ...*......
// ..35..633.
// ......#...
// 617*......
// .....+.58.
// ..592.....
// ......755.
// ...$.*....
// .664.598..
//
// In this schematic, there are two gears. The first is in the top left; it has part numbers 467
// and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is
// 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.)
// Adding up all of the gear ratios produces 467835.
//
// What is the sum of all of the gear ratios in your engine schematic?

// use colored::*;

struct Schematic {
    height: usize,
    width: usize,
    map: Vec<Vec<char>>,
}

fn parse_schematic(schematic: &str) -> Schematic {
    let mut height = 0;
    let mut width = 0;
    let mut lines: Vec<Vec<char>> = vec![];

    for line in schematic.lines() {
        height += 1;
        let mut schematic_line: Vec<char> = vec![];

        for character in line.chars() {
            if height == 1 {
                width += 1;
            }
            schematic_line.push(character);
        }
        lines.push(schematic_line);
    }

    Schematic {
        height,
        width,
        map: lines,
    }
}

fn get_number_at(x: usize, y: usize, schematic_map: &Schematic) -> Option<u32> {
    let mut current_x = x;

    if !schematic_map.map[y][current_x].is_numeric() {
        return None;
    }

    while current_x != 0 && schematic_map.map[y][current_x - 1].is_numeric() {
        current_x -= 1;
    }

    let mut number_string = "".to_string();

    while current_x < schematic_map.width && schematic_map.map[y][current_x].is_numeric() {
        number_string.push(schematic_map.map[y][current_x]);
        current_x += 1;
    }

    Some(number_string.parse::<u32>().unwrap())
}

fn get_numbers_around(x: usize, y: usize, schematic_map: &Schematic) -> Vec<u32> {
    let mut unique_number_positions: Vec<u32> = vec![];

    if y > 0 {
        if schematic_map.map[y - 1][x].is_numeric() {
            unique_number_positions.push(get_number_at(x, y - 1, schematic_map).unwrap());
        } else {
            if x > 0 && schematic_map.map[y - 1][x - 1].is_numeric() {
                unique_number_positions.push(get_number_at(x - 1, y - 1, schematic_map).unwrap());
            }
            if x < schematic_map.width - 1 && schematic_map.map[y - 1][x + 1].is_numeric() {
                unique_number_positions.push(get_number_at(x + 1, y - 1, schematic_map).unwrap());
            }
        }
    }

    if x > 0 && schematic_map.map[y][x - 1].is_numeric() {
        unique_number_positions.push(get_number_at(x - 1, y, schematic_map).unwrap());
    }

    if x < schematic_map.width - 1 && schematic_map.map[y][x + 1].is_numeric() {
        unique_number_positions.push(get_number_at(x + 1, y, schematic_map).unwrap());
    }

    if y < schematic_map.height - 1 {
        if schematic_map.map[y + 1][x].is_numeric() {
            unique_number_positions.push(get_number_at(x, y + 1, schematic_map).unwrap());
        } else {
            if x > 0 && schematic_map.map[y + 1][x - 1].is_numeric() {
                unique_number_positions.push(get_number_at(x - 1, y + 1, schematic_map).unwrap());
            }
            if x < schematic_map.width - 1 && schematic_map.map[y + 1][x + 1].is_numeric() {
                unique_number_positions.push(get_number_at(x + 1, y + 1, schematic_map).unwrap());
            }
        }
    }

    unique_number_positions
}

fn get_gear_ratio(x: usize, y: usize, schematic_map: &Schematic) -> u32 {
    let numbers_around = get_numbers_around(x, y, schematic_map);

    if numbers_around.len() == 2 {
        return numbers_around[0] * numbers_around[1];
    }

    0
}

pub fn part_1(schematic: &str) -> (u32, u32) {
    let schematic_map = parse_schematic(schematic);

    let mut in_number = false;
    let mut current_is_part_number = false;
    let mut potential_part_number = "".to_string();
    let mut sum = 0;
    let mut sum_gear_ratio = 0;

    for (y, line) in schematic_map.map.iter().enumerate() {
        for (x, character) in line.iter().enumerate() {
            if character.is_numeric() {
                in_number = true;

                potential_part_number.push(*character);
                current_is_part_number =
                    current_is_part_number || is_part_of_partnumber(x, y, &schematic_map);
            } else {
                if in_number {
                    let current_number = potential_part_number.parse::<u32>().unwrap();
                    if current_is_part_number {
                        sum += current_number;
                        // print!("{}", current_number.to_string().white().on_red());
                    } // else {
                      // print!("{}", current_number.to_string().white());
                      // }
                    in_number = false;
                    potential_part_number = "".to_string();
                    current_is_part_number = false;
                }

                // if character == &'.' {
                // print!("{}", ".".bright_black());
                // } else
                if character == &'*' {
                    let gear_ratio = get_gear_ratio(x, y, &schematic_map);
                    sum_gear_ratio += gear_ratio;

                    // if gear_ratio == 0 {
                    //     print!("{}", "*".white().on_green());
                    // } else {
                    //     print!("{}", "*".white().on_blue());
                    // }
                } // else {
                  // print!("{}", character.to_string().red().on_yellow());
                  // }
            }
        }
        if in_number {
            let current_number = potential_part_number.parse::<u32>().unwrap();
            if current_is_part_number {
                sum += current_number;
                // print!("{}", current_number.to_string().blue().on_red());
            } // else {
              // print!("{}", current_number.to_string().green());
              // }
            current_is_part_number = false;
        }

        in_number = false;
        potential_part_number = "".to_string();

        // println!();
    }
    (sum, sum_gear_ratio)
}

fn is_part_of_partnumber(x: usize, y: usize, schematic_map: &Schematic) -> bool {
    if x >= schematic_map.width || y >= schematic_map.height {
        return false;
    }
    // println!("check for {}:{}", x, y);

    let x_lower = if x == 0 { 0 } else { x - 1 };
    let y_lower = if y == 0 { 0 } else { y - 1 };

    for check_y in y_lower..y + 2 {
        for check_x in x_lower..x + 2 {
            // println!("checking {}:{}", check_x, check_y);
            if check_x == x && check_y == y {
                // println!("same spot, skipping");
                continue;
            }

            if check_x >= schematic_map.width || check_y >= schematic_map.height {
                // println!("out of bounds, skipping");
                continue;
            }

            let character = schematic_map.map[check_y][check_x];
            // println!("character to check: {}", character);

            if character != '.' && !character.is_numeric() {
                // println!("{} is a symbol", character);
                return true;
            }
        }
    }
    false
}

#[cfg(test)]
mod test {
    use super::*;

    static SCHEMATIC_STR: &str = "467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..";

    #[test]
    fn test_is_part_of_partnumber() {
        let schematic_map = parse_schematic(SCHEMATIC_STR);

        assert!(
            !is_part_of_partnumber(0, 0, &schematic_map),
            "top corner is not part number"
        );
        assert!(
            !is_part_of_partnumber(schematic_map.width, schematic_map.height, &schematic_map),
            "outside of schematic should be false"
        );
        assert!(
            is_part_of_partnumber(2, 0, &schematic_map),
            "diagonal from first line should be part number"
        );
        assert!(
            is_part_of_partnumber(2, 2, &schematic_map),
            "diagonal should be part number"
        );
        assert!(
            !is_part_of_partnumber(1, 3, &schematic_map),
            "another number is not a symbol"
        );
        assert!(
            !is_part_of_partnumber(
                schematic_map.width - 1,
                schematic_map.height - 1,
                &schematic_map
            ),
            "the last corner does not have any symbol next to it"
        );
    }

    #[test]
    fn test_get_gear_ratio() {
        let schematic_map = parse_schematic(SCHEMATIC_STR);

        assert_eq!(0, get_gear_ratio(0, 0, &schematic_map));

        assert_eq!(467 * 35, get_gear_ratio(3, 1, &schematic_map));

        assert_eq!(0, get_gear_ratio(3, 4, &schematic_map));

        assert_eq!(755 * 598, get_gear_ratio(5, 8, &schematic_map));
    }

    #[test]
    fn test_part_1() {
        assert_eq!((4361, 467835), part_1(SCHEMATIC_STR));
    }

    #[test]
    fn test_get_number_at() {
        let schematic_map = parse_schematic(SCHEMATIC_STR);
        assert_eq!(None, get_number_at(0, 1, &schematic_map));
        assert_eq!(Some(467), get_number_at(0, 0, &schematic_map));
        assert_eq!(Some(114), get_number_at(5, 0, &schematic_map));
        assert_eq!(Some(467), get_number_at(1, 0, &schematic_map));
        assert_eq!(Some(467), get_number_at(2, 0, &schematic_map));
        assert_eq!(Some(35), get_number_at(2, 2, &schematic_map));
        assert_eq!(Some(35), get_number_at(3, 2, &schematic_map));
        assert_eq!(Some(633), get_number_at(6, 2, &schematic_map));
        assert_eq!(Some(633), get_number_at(7, 2, &schematic_map));
        assert_eq!(Some(633), get_number_at(8, 2, &schematic_map));
    }

    #[test]
    fn test_unique_numbers_around() {
        let schematic_map = parse_schematic(SCHEMATIC_STR);

        assert_eq!(vec![] as Vec<u32>, get_numbers_around(0, 2, &schematic_map));
        assert_eq!(vec![114], get_numbers_around(8, 0, &schematic_map));
        assert_eq!(vec![467, 35], get_numbers_around(3, 1, &schematic_map));
        assert_eq!(vec![617], get_numbers_around(3, 4, &schematic_map));
        assert_eq!(vec![755, 598], get_numbers_around(5, 8, &schematic_map));
        assert_eq!(vec![664, 598], get_numbers_around(4, 8, &schematic_map));
    }
}
