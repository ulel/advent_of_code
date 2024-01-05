use std::str::FromStr;

pub fn part_1(input: &str) -> u32 {
    input
        .lines()
        .map(|line| line.parse::<Card>().unwrap())
        .map(|card| card.score())
        .sum()
}

pub fn part_2(input: &str) -> u32 {
    let mut cards: Vec<Card> = input
        .lines()
        .map(|line| line.parse::<Card>().unwrap())
        .collect();

    let mut total_copies = 0;

    for i in 0..cards.len() {
        let card = &cards[i];
        total_copies += card.copies;
        let first_to_update = i + 1;
        let last_to_update = i + 1 + (cards[i].matches as usize);
        for j in first_to_update..last_to_update {
            cards[j].copies += cards[i].copies
        }
    }

    total_copies
}

#[derive(Debug, PartialEq)]
struct Card {
    id: u32,
    numbers: Vec<u32>,
    mine: Vec<u32>,
    matches: u32,
    copies: u32,
}

impl Card {
    fn score(&self) -> u32 {
        if self.matches > 0 {
            2_u32.pow(self.matches - 1)
        } else {
            0
        }
    }
}

#[derive(Debug, PartialEq, Eq)]
struct ParseCardError {
    message: String,
}

impl FromStr for Card {
    type Err = ParseCardError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let (id_str, rest) = s
            .strip_prefix("Card ")
            .and_then(|s| s.split_once(':'))
            .ok_or(ParseCardError {
                message: format!("Extract id failed {s}").to_string(),
            })?;

        let (number_str, mine_str) = rest.split_once('|').ok_or(ParseCardError {
            message: format!("Split failed {s}").to_string(),
        })?;

        let numbers: Vec<u32> = number_str
            .split(' ')
            .filter_map(|number| number.parse::<u32>().ok())
            .collect();
        let mine: Vec<u32> = mine_str
            .split(' ')
            .filter_map(|mine| mine.parse::<u32>().ok())
            .collect();

        let matches = mine.iter().filter(|x| numbers.contains(x)).count() as u32;

        Ok(Card {
            id: match id_str.trim().parse::<u32>() {
                Ok(id) => id,
                Err(_err) => {
                    return Err(ParseCardError {
                        message: format!("Parsing id failed {id_str} {s}").to_string(),
                    })
                }
            },
            numbers,
            mine,
            matches,
            copies: 1,
        })
    }
}

#[cfg(test)]
mod test {
    use std::collections::HashMap;

    use super::*;
    use rstest::*;

    #[fixture]
    fn expected_cards() -> HashMap<u32, Card> {
        HashMap::from([
            (
                1,
                Card {
                    id: 1,
                    numbers: vec![41, 48, 83, 86, 17],
                    mine: vec![83, 86, 6, 31, 17, 9, 48, 53],
                    matches: 4,
                    copies: 1,
                },
            ),
            (
                2,
                Card {
                    id: 2,
                    numbers: vec![13, 32, 20, 16, 61],
                    mine: vec![61, 30, 68, 82, 17, 32, 24, 19],
                    matches: 2,
                    copies: 1,
                },
            ),
            (
                3,
                Card {
                    id: 3,
                    numbers: vec![1, 21, 53, 59, 44],
                    mine: vec![69, 82, 63, 72, 16, 21, 14, 1],
                    matches: 2,
                    copies: 1,
                },
            ),
            (
                4,
                Card {
                    id: 4,
                    numbers: vec![41, 92, 73, 84, 69],
                    mine: vec![59, 84, 76, 51, 58, 5, 54, 83],
                    matches: 1,
                    copies: 1,
                },
            ),
            (
                5,
                Card {
                    id: 5,
                    numbers: vec![87, 83, 26, 28, 32],
                    mine: vec![88, 30, 70, 12, 93, 22, 82, 36],
                    matches: 0,
                    copies: 1,
                },
            ),
            (
                6,
                Card {
                    id: 6,
                    numbers: vec![31, 18, 13, 56, 72],
                    mine: vec![74, 77, 10, 23, 35, 67, 36, 11],
                    matches: 0,
                    copies: 1,
                },
            ),
        ])
    }
    #[rstest]
    #[case("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", 1)]
    #[case("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19", 2)]
    #[case("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1", 3)]
    #[case("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83", 4)]
    #[case("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36", 5)]
    #[case("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11", 6)]
    fn test_get_card_from_line(
        #[case] input: &str,
        #[case] card_id: u32,
        expected_cards: HashMap<u32, Card>,
    ) {
        assert_eq!(expected_cards[&card_id], input.parse().unwrap());
    }

    /// In the above example, card 1 has five winning numbers (41, 48, 83, 86, and 17) and eight numbers
    /// you have (83, 86, 6, 31, 17, 9, 48, and 53). Of the numbers you have, four of them (48, 83, 17,
    /// and 86) are winning numbers! That means card 1 is worth 8 points (1 for the first match, then
    /// doubled three times for each of the three matches after the first).
    ///
    ///     Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
    ///     Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
    ///     Card 4 has one winning number (84), so it is worth 1 point.
    ///     Card 5 has no winning numbers, so it is worth no points.
    ///     Card 6 has no winning numbers, so it is worth no points.
    ///
    /// So, in this example, the Elf's pile of scratchcards is worth 13 points.
    ///
    #[rstest]
    #[case(1, 8)]
    #[case(2, 2)]
    #[case(3, 2)]
    #[case(4, 1)]
    #[case(5, 0)]
    #[case(6, 0)]
    fn test_calculate_score_for_card(
        #[case] card_id: u32,
        #[case] expected_points: u32,
        expected_cards: HashMap<u32, Card>,
    ) {
        assert_eq!(expected_points, expected_cards[&card_id].score());
    }

    #[fixture]
    fn test_input() -> &'static str {
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
    }

    #[rstest]
    fn test_part_1(test_input: &str) {
        assert_eq!(13, part_1(test_input));
    }

    #[rstest]
    fn test_part_2(test_input: &str) {
        assert_eq!(30, part_2(test_input));
    }
}
