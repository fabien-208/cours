-- exercice 1
estPremier :: Int -> Int -> Bool

estPremier nb 1 = True
estPremier nb d = 
    if mod nb d == 0
        then False
        else estPremier (nb-1) d


main :: IO ()
main = do
    putStrLn "Entrez un chiffre"
    saisie <- getLine
    let lis = read saisie in
        print(estPremier lis lis)

-- exercice 2

resultatManche :: (String, String) -> Int
resultatManche =
    if a == "Pierre"
        then if b == "Feuille"
            then -1
            else 0
        else  if b == "Pierre"
            then 0
            else 1