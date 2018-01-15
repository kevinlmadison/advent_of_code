module Main where

parse xs = [read(x) :: Integer | x <- xs]

main :: IO ()
main = do
    s <- parse . lines <$> readFile "input.txt"
    print $ map part_1 s
