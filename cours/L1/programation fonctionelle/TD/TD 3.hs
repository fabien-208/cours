estPremier :: Int -> Int -> Bool

estPremier nb 1 = True
estPremier nb d = 
    (mod d nb /= 0) && estPremier nb (d - 1)


main :: IO ()
main = do
    putStrLn "Entrez un chiffre"
    saisie <- getLine
    let lis = read saisie in
        print(estPremier lis lis)


