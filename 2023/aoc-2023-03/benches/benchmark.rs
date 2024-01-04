use aoc_2023_03::*;

fn main() {
    // Run registered benchmarks.
    divan::main();
}

// Define a `fibonacci` function and register it for benchmarking.
#[divan::bench]
fn solve() {
    solver::part_1(divan::black_box(include_str!("../resources/input")));
}
