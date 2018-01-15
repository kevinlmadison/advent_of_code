module Main where
import System.Environment
import Data.List
import Data.Char

--I DID NOT CREATE ANY OF THIS, I FOUND ALL OF IT ON REDDIT AND WANTED TO EXPERIMENT WITH HASKELL

{-
solve n xs = [sum $ zipWith (\a b -> if a == b then a else 0) xs (drop n $ cycle xs)]
solve1 = solve 1

main :: IO ()
main = do
    contents <- getContents
    print $ show $ solve1 $ read contents
-}

--I DID NOT CREATE ANY OF THIS, I FOUND ALL OF IT ON REDDIT AND WANTED TO EXPERIMENT WITH HASKELL
main = do
    -- the <$> is an infix alias for fmap
    -- the init is how we're getting rid of the \n
    s <- init <$> readFile "input.txt"
    print $ process 1 $ s ++ [head s]
    let
      l = length $ s
      ll = div l 2
    print $ process ll $ s ++ take ll s

process k s =
    sum . map (read . (:[]) . fst) . filter (uncurry (==)) $ zip s (drop k s)
