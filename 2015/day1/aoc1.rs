
fn main() {
    let mut floor = 0;
    let mut count = 0;
    let f = include_str!("aoc1.txt");
    let dirs = f.split("").map(|x| x.trim());
    for dir in dirs {
        if dir == '('.to_string() {
            floor += 1;
        }
        if dir == ')'.to_string() {
            floor -= 1;
        }
        count += 1;
        if floor < 0 {
            break;
        }
    println!("step: {}  floor: {}", count, floor);
    }
}
