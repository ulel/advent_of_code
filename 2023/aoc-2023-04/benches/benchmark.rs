use aoc_2023_04::*;

fn main() {
    divan::main();
}

#[divan::bench]
fn part_1() {
    solver::part_1(divan::black_box(include_str!("../resources/input")));
}

#[divan::bench]
fn part_2() {
    solver::part_1(divan::black_box(include_str!("../resources/input")));
}
