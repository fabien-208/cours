
positif :: [Int] -> [Int] -> [Int]
positif [] [] = []
positif l (x:xs) = 
    if x > 0
        then positif (x:l) xs
        else positif l xs


main :: IO ()
main = do
    putStrLn "Entrez une liste de chiffre"
    saisie <- getLine
    let lis = read saisie in
        print(positif [] lis)


