// --- Day 2: Cube Conundrum ---
// 
// You're launched high into the atmosphere! The apex of your trajectory just barely reaches the
// surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's
// quite cold, but you don't see much snow. An Elf runs over to greet you.
// 
// The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll
// be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't
// get many visitors up here; would you like to play a game in the meantime?
// 
// As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue.
// Each time you play this game, he will hide a secret number of cubes of each color in the bag,
// and your goal is to figure out information about the number of cubes.
// 
// To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab
// a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a
// few times per game.
// 
// You play several games and record the information from each game (your puzzle input). Each game
// is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated
// list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).
// 
// For example, the record of a few games might look like this:
// 
// Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
// Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
// Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
// Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
// Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
// 
// In game 1, three sets of cubes are revealed from the bag (and then put back again). The first
// set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue
// cubes; the third set is only 2 green cubes.
// 
// The Elf would first like to know which games would have been possible if the bag contained only
// 12 red cubes, 13 green cubes, and 14 blue cubes?
// 
// In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with
// that configuration. However, game 3 would have been impossible because at one point the Elf
// showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the
// Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been
// possible, you get 8.
// 
// Determine which games would have been possible if the bag had been loaded with only 12 red
// cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

// --- Part Two ---

// The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure
// why the water stopped; however, he can show you how to get to the water source to check it out
// for yourself. It's just up ahead!
// 
// As you continue your walk, the Elf poses a second question: in each game you played, what is the
// fewest number of cubes of each color that could have been in the bag to make the game possible?
// 
// Again consider the example games from earlier:
// 
// Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
// Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
// Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
// Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
// Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
// 
//     In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes.
//                If any color had even one fewer cube, the game would have been impossible.
//     Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
//     Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
//     Game 4 required at least 14 red, 3 green, and 15 blue cubes.
//     Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
// 
// The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied
// together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560,
// 630, and 36, respectively. Adding up these five powers produces the sum 2286.
// 
// For each game, find the minimum set of cubes that must have been present. What is the sum of the
// power of these sets?

use std::cmp::max;

fn main() {
    let input = include_str!("../resources/input");
    let games = parse_games(input);

    println!("Part 1: {}", part_1(&games));
    println!("Part 2: {}", part_2(&games));
}

fn part_1(games: &Vec<Game>) -> u32 {
    sum_valid_games(games)
}

fn part_2(games: &Vec<Game>) -> u32 {
    sum_powers(games)
}

fn parse_games(input: &str) -> Vec<Game> {
    let mut games: Vec<Game> = vec![];
    for line in input.lines() {
        games.push(parse_game(line));
    }
    return games;
}

fn parse_game(game_line: &str) -> Game
{
    let mut found_id: bool = false;
    let mut parsing_id: bool = false;
    let mut current_token: String = "".to_string();

    let mut looking_for_number: bool = false;
    let mut parsing_number: bool = false;

    let mut looking_for_color: bool = false;
    let mut parsing_color: bool = false;

    let mut current_number: u32 = 0;

    let mut current_set = Set {
        reds: 0,
        greens: 0,
        blues: 0,
    };

    let mut game = Game {
        id: 0,
        sets: vec![],
    };

    for character in game_line.chars() {
        if !found_id && !parsing_id  {
            if character == ' ' {
                parsing_id = true;
            }
        } else if !found_id && parsing_id {
            if character == ':' {
                game.id = current_token.parse::<u32>().unwrap();
                found_id = true;
                current_token = "".to_string();

                looking_for_number = true;
            } else {
                current_token = format!("{}{}", current_token, character);
            }
        } else if looking_for_number {
            if character != ' ' {
                current_token = format!("{}{}", current_token, character);
                looking_for_number = false;
                parsing_number = true;
            }
        } else if parsing_number {
            if character == ' ' {
                current_number = current_token.parse::<u32>().unwrap();
                parsing_number = false;
                looking_for_color = true;
                current_token = "".to_string();
            } else {
                current_token = format!("{}{}", current_token, character);
            }
        } else if looking_for_color {
            if character != ' ' {
                current_token = format!("{}{}", current_token, character);
                looking_for_color = false;
                parsing_color = true;
            }
        } else if parsing_color {
            if character == ';' || character == ',' {
                if current_token == "red" {
                    current_set.reds = current_number;
                } else if current_token == "green" {
                    current_set.greens = current_number;
                } else if current_token == "blue" {
                    current_set.blues = current_number;
                }

                if character == ';' {
                    game.sets.push(current_set);
                    current_set = Set{
                        reds: 0,
                        greens: 0,
                        blues: 0,
                    };
                }

                parsing_color = false;
                looking_for_number = true;

                current_token = "".to_string();
            } else {
                current_token = format!("{}{}", current_token, character);
            }
        }
    }

    if current_token == "red" {
        current_set.reds = current_number;
    } else if current_token == "green" {
        current_set.greens = current_number;
    } else if current_token == "blue" {
        current_set.blues = current_number;
    }

    game.sets.push(current_set);

    game
}

fn is_valid_game(game: &Game) -> bool {
    let limit_red = 12;
    let limit_green = 13;
    let limit_blue = 14;

    for set in &game.sets {
        if set.reds > limit_red || set.greens > limit_green || set.blues > limit_blue {
            return false;
        }
    }

    true
}

fn sum_valid_games(games: &Vec<Game>) -> u32 {
    games.iter().filter(|game| is_valid_game(game)).map(|game| game.id).sum()
}

fn sum_powers(games: &Vec<Game>) -> u32 {
    games.iter().map(|game| power_of_game(game)).sum()
}

fn power_of_game(game: &Game) -> u32 {
    let mut min_red = 0;
    let mut min_green = 0;
    let mut min_blue = 0;

    for set in &game.sets {
        min_red = max(min_red, set.reds);
        min_green = max(min_green, set.greens);
        min_blue = max(min_blue, set.blues);
    }

    min_red * min_green * min_blue
}

#[derive(PartialEq)]
#[derive(Debug)]
struct Set {
    reds: u32,
    greens: u32,
    blues: u32,
}

struct Game {
    id: u32,
    sets: Vec<Set>,
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parse_id_for_game_1() {
        let line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green";
        let result = parse_game(line);

        assert_eq!(result.id, 1);
    }

    #[test]
    fn test_parse_id_for_game_98() {
        let line = "Game 98: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green";
        let result = parse_game(line);

        assert_eq!(result.id, 98);
    }

    #[test]
    fn test_parse_game_1() {
        let line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green";
        let result = parse_game(line);

        let expected_sets = vec![
            Set {
                reds: 4,
                greens: 0,
                blues: 3,
            },
            Set {
                reds: 1,
                greens: 2,
                blues: 6,
            },
            Set {
                reds: 0,
                greens: 2,
                blues: 0,
            },
        ];

        assert_eq!(result.id, 1);
        assert_eq!(result.sets, expected_sets);
    }

    #[test]
    fn test_parse_game_2() {
        let line = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue";
        let result = parse_game(line);

        let expected_sets = vec![
            Set {
                reds: 0,
                greens: 2,
                blues: 1,
            },
            Set {
                reds: 1,
                greens: 3,
                blues: 4,
            },
            Set {
                reds: 0,
                greens: 1,
                blues: 1,
            },
        ];

        assert_eq!(result.id, 2);
        assert_eq!(result.sets, expected_sets);
    }

    #[test]
    fn test_parse_game_3() {
        let line = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red";
        let result = parse_game(line);

        let expected_sets = vec![
            Set {
                reds: 20,
                greens: 8,
                blues: 6,
            },
            Set {
                reds: 4,
                greens: 13,
                blues: 5,
            },
            Set {
                reds: 1,
                greens: 5,
                blues: 0,
            },
        ];

        assert_eq!(result.id, 3);
        assert_eq!(result.sets, expected_sets);
    }

    #[test]
    fn test_parse_game_4() {
        let line = "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red";
        let result = parse_game(line);

        let expected_sets = vec![
            Set {
                reds: 3,
                greens: 1,
                blues: 6,
            },
            Set {
                reds: 6,
                greens: 3,
                blues: 0,
            },
            Set {
                reds: 14,
                greens: 3,
                blues: 15,
            },
        ];

        assert_eq!(result.id, 4);
        assert_eq!(result.sets, expected_sets);
    }

    #[test]
    fn test_parse_game_5() {
        let line = "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green";
        let result = parse_game(line);

        let expected_sets = vec![
            Set {
                reds: 6,
                greens: 3,
                blues: 1,
            },
            Set {
                reds: 1,
                greens: 2,
                blues: 2,
            }
        ];

        assert_eq!(result.id, 5);
        assert_eq!(result.sets, expected_sets);
    }

    #[test]
    fn test_valid_game()
    {
        let valid_game = Game {
            id: 10,
            sets: vec![Set {
                reds: 12,
                greens: 3,
                blues: 1,
            },
            Set {
                reds: 1,
                greens: 13,
                blues: 2,
            },
            Set {
                reds: 0,
                greens: 0,
                blues: 14,
            }],
        };

        assert_eq!(true, is_valid_game(&valid_game));
    }

    #[test]
    fn test_invalid_game_1()
    {
        let invalid_game = Game {
            id: 10,
            sets: vec![Set {
                reds: 13,
                greens: 3,
                blues: 1,
            },
            Set {
                reds: 1,
                greens: 2,
                blues: 2,
            },
            Set {
                reds: 0,
                greens: 0,
                blues: 0,
            }],
        };

        assert_eq!(false, is_valid_game(&invalid_game));
    }

    #[test]
    fn test_invalid_game_2()
    {
        let invalid_game = Game {
            id: 10,
            sets: vec![Set {
                reds: 6,
                greens: 3,
                blues: 1,
            },
            Set {
                reds: 1,
                greens: 14,
                blues: 2,
            },
            Set {
                reds: 0,
                greens: 0,
                blues: 0,
            }],
        };

        assert_eq!(false, is_valid_game(&invalid_game));
    }

    #[test]
    fn test_invalid_game_3()
    {
        let invalid_game = Game {
            id: 10,
            sets: vec![Set {
                reds: 6,
                greens: 3,
                blues: 1,
            },
            Set {
                reds: 1,
                greens: 2,
                blues: 2,
            },
            Set {
                reds: 0,
                greens: 0,
                blues: 15,
            }],
        };

        assert_eq!(false, is_valid_game(&invalid_game));
    }

    #[test]
    fn test_sum_valid_ids()
    {
        let invalid_games = vec![
        Game {
            id: 1,
            sets: vec![Set {
                reds: 13,
                greens: 3,
                blues: 1,
            },
            Set {
                reds: 1,
                greens: 2,
                blues: 2,
            },
            Set {
                reds: 0,
                greens: 0,
                blues: 0,
            }],
        },
        Game {
            id: 2,
            sets: vec![Set {
                reds: 13,
                greens: 3,
                blues: 1,
            },
            Set {
                reds: 1,
                greens: 2,
                blues: 2,
            },
            Set {
                reds: 0,
                greens: 0,
                blues: 0,
            }],
        },
        Game {
            id: 3,
            sets: vec![Set {
                reds: 13,
                greens: 3,
                blues: 1,
            },
            Set {
                reds: 1,
                greens: 2,
                blues: 2,
            },
            Set {
                reds: 0,
                greens: 0,
                blues: 0,
            }],
        },
        ];

        let valid_games = vec![
        Game {
            id: 4,
            sets: vec![Set {
                reds: 12,
                greens: 3,
                blues: 1,
            },
            Set {
                reds: 1,
                greens: 2,
                blues: 2,
            },
            Set {
                reds: 0,
                greens: 0,
                blues: 0,
            },
            ],
        },
        Game {
            id: 5,
            sets: vec![Set {
                reds: 12,
                greens: 3,
                blues: 1,
            },
            Set {
                reds: 1,
                greens: 2,
                blues: 2,
            },
            Set {
                reds: 0,
                greens: 0,
                blues: 0,
            },
            ],
        },
        ];

        let mut all_games: Vec<Game> = vec![];

        all_games.extend(valid_games);
        all_games.extend(invalid_games);

        assert_eq!(9, sum_valid_games(&all_games));
    }

    #[test]
    fn test_power_of_game()
    {
        let game_1 = Game {
            id: 1,
            sets: vec![Set {
                reds: 13,
                greens: 3,
                blues: 1,
            },
            Set {
                reds: 1,
                greens: 2,
                blues: 2,
            },
            Set {
                reds: 0,
                greens: 0,
                blues: 0,
            }],
        };
        assert_eq!(13*3*2, power_of_game(&game_1));

        let game_2 = Game {
            id: 2,
            sets: vec![Set {
                reds: 10,
                greens: 3,
                blues: 1,
            },
            Set {
                reds: 1,
                greens: 5,
                blues: 2,
            },
            Set {
                reds: 0,
                greens: 0,
                blues: 99,
            }],
        };
        assert_eq!(10*5*99, power_of_game(&game_2));
    }
}
