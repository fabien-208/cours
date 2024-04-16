minrec :: [Int] -> Int
minrec [] = 0
minrec l =
    minrec' (head l) l



minrec' :: Int -> [Int] -> Int
minrec' n (x:xs) =
    if x < n
        then minrec' x xs
        else minrec' n xs

minfoldr :: [Int] -> Int
minfoldr [] = 0
minfoldr l =
    foldr min (head l) l


main :: IO ()
main = do
    putStrLn "Entrez une liste de chiffre"
    saisie <- getLine
    let lis = read saisie in
        print(minfoldr lis)


