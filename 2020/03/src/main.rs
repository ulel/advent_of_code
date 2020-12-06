/*
--- Day 3: Toboggan Trajectory ---

With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan
might be easy, it's certainly not safe: there's very minimal steering and the area is covered in
trees. You'll need to see which angles will take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You
make a map (your puzzle input) of the open squares (.) and trees (#) you can see. For example:

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#

These aren't the only trees, though; due to something you read about once involving arboreal
genetics and biome stability, the same pattern repeats to the right many times:

..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

You start on the open square (.) in the top-left corner and need to reach the bottom (below the
bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers
rational numbers); start by counting all the trees you would encounter for the slope right 3, down
1:

From your starting position at the top-left, check the position that is right 3 and down 1. Then,
check the position that is right 3 and down 1 from there, and so on until you go past the bottom of
the map.

The locations you'd check in the above example are marked here with O where there was an open
square and X where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

In this example, traversing the map using this slope would cause you to encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many
trees would you encounter?

--- Part Two ---

Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal
stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start
at the top-left corner and traverse the map all the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied
together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed
slopes?
*/

use std::fs::File;
use std::io::{self, BufRead};

fn main() {
    let map = build_map();
    let part_1_collisions = calculate_collisions(3, 1, &map);

    println!("Part 1: {}", part_1_collisions);

    let part_2_slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]];

    let mut part_2_answer = 1;

    for current_slope in &part_2_slopes {
        part_2_answer =
            part_2_answer * calculate_collisions(current_slope[0], current_slope[1], &map);
    }

    println!("Part 2: {}", part_2_answer);
}

fn calculate_collisions(slope_x: usize, slope_y: usize, map: &Vec<Vec<bool>>) -> u32 {
    let mut current_x = 0;
    let mut current_y = 0;
    let mut collisions = 0;

    let width = map[0].len();

    while current_y < map.len() {
        if map[current_y][current_x] {
            collisions += 1;
        }
        current_y += slope_y;
        current_x += slope_x;

        if current_x >= width {
            current_x = current_x - width;
        }
    }

    collisions
}

fn build_map() -> Vec<Vec<bool>> {
    let mut map: Vec<Vec<bool>> = Vec::new();

    let input_file = File::open("input").expect("input file could not be opened");
    let file_reader = io::BufReader::new(input_file);
    let lines = file_reader.lines();

    for line in lines {
        map.push(build_map_line(&line.unwrap()));
    }
    map
}

fn build_map_line(line: &String) -> Vec<bool> {
    let mut map_line: Vec<bool> = Vec::new();

    for map_symbol in line.chars() {
        if map_symbol == '#' {
            map_line.push(true);
        } else {
            map_line.push(false);
        }
    }

    map_line
}
