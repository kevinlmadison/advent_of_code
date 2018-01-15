use std::fs::File;
use std::io::Read;


fn main() {
    let mut data = String::new();
    let mut f = File::open("input.txt").unwrap();

    f.read_to_string(&mut data).unwrap();
    let input: Vec<_> = data
        .chars()
        .filter_map(|c| c.to_digit(10))
        .collect();

    let result: u32 = part_one(&input);
    println!("result p1: {}", result);

    let result: u32 = part_two(&input);
    println!("result p2: {}", result);
}

fn part_one(data: &Vec<u32>) -> u32 {
    data.iter()
        .zip(data.iter().cycle().skip(1))
        .filter_map(|(a, b)| if a == b { Some(a) } else { None })
        .sum()
}

fn part_two(data: &Vec<u32>) -> u32 {
    data.iter()
        .zip(data.iter().cycle().skip(data.len()/2))
        .filter_map(|(a, b)| if a == b { Some(a) } else { None })
        .sum()
}
