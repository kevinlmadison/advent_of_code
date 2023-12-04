# use `nix eval -f .` to view output

let
  inherit (import ../aoc-utils.nix) min lib sum minInt max;
  inherit (lib.strings) toInt splitString;
  inherit (lib.lists) foldr take;
  inherit (builtins) substring readFile split sort length stringLength;
  input = readFile ./input;
  splitList = splitString "\n\n" (substring 0 ((stringLength input) - 1) input);
  cals = map (str: sum (map toInt (splitString "\n" str))) splitList;
  part1 = max cals;
  part2 = sum(take 3 (sort (a: b: a > b) cals));
in {
  inherit part1;
  inherit part2;
}

