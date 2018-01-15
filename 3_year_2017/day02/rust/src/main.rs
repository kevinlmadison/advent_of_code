extern crate itertools;

//use std::fs::File;
//use std::io::Read;
use itertools::Itertools;

fn main() {
    /*
    let mut data = String::new();
    let mut f = File::open("input.txt").expect("Failed to open file");

    f.read_to_string(&mut data).expect("Failed to read file");
    */
    let data = include_str!("../input.txt");
    let input: Vec<Vec<u32>> = data.lines()
        .map(|line|
             line
                .split_whitespace()
                .filter_map(|n| n.parse::<u32>().ok())
                .collect())
        .collect();

    let tot: u32 = part_one(&input);
    println!("result p1: {}", tot);

    let tot: u32 = part_two(&input);
    println!("result p2: {}", tot);
}

fn part_one(input: &Vec<Vec<u32>>) -> u32 {
    input.iter()
        .map(|line| line.iter().max().unwrap() - line.iter().min().unwrap())
        .sum()
}

fn part_two(input: &Vec<Vec<u32>>) -> u32 {
    input.iter()
        .filter_map(|line| 
                    line.iter()
                    .tuple_combinations()
                    .filter_map(|(a, b)| {
                        if a % b == 0 {
                            Some(a / b)
                        } else if b % a == 0 {
                            Some(b / a)
                        } else {
                            None
                        }
                    })
                    .next())
        .sum()
}
