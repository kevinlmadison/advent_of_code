module Main where

read_in :: [String] -> [[Integer]]
read_in s = [[read(x) :: Integer | x <- words y] | y <- s]

part_1 :: Integral a => [a] -> a
part_1 xs = (maximum xs) - (minimum xs)

part_2 :: Integral a => [a] -> a
part_2 xs = head [x `div` y | x <- xs, y <- xs, x /= y && x `mod` y == 0] 

main :: IO ()
main = do
    s <- read_in . lines <$> readFile "input.txt"
    print $ sum $ map part_1 s
    print $ sum $ map part_2 s
