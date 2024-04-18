fibo :: Int -> Int
fibo 0 = 0
fibo 1 = 1
fibo n = fibo(n-1) + fibo(n-2)




main :: IO ()
main = do
    putStrLn "Entrez une valeur numérique"
    saisie <- getLine -- saisit une chaîne au clavier
    let n = read saisie in --  convertit la saisie en Int
        print(fibo n)