module Main where

import Data.List

parse = lines <$> readFile "input.txt"

p1 xs = if (length $ nub xs) == (length xs) then 1 else 0
p2 xs = if (length $ nub [sort x | x <- xs]) == (length xs) then 1 else 0

main = do
    xs <- parse
    print $ sum $ map p1 (map words xs)
    print $ sum $ map p2 (map words xs)
    print "done"
