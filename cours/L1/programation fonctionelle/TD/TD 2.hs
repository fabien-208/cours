-- exercice 1 
compter1 :: [Int] -> Int
compter1 l = compter1' l (l!!0)

compter1' :: [Int] -> Int -> Int
compter1' (x:xs) n =
    if x ==1 
        then compter1' xs n+1
        else compter1' xs n


compter2 :: [Int] -> Int
compter2 (x:xs) = 
    if x == 1
        then 1+compter2 xs
        else compter2 xs


voirure :: Int -> [Int] -> Int
voirure n (x:xs) = 
    if x == n
        then 1 + voirure n xs
        else voirure n xs


erUns :: [Int] -> Int
erUns l = voirure 1 l


--exercice 2

moyenne :: [Int] -> Int
moyenne [] = 0
moyenne l = (sommme 0 l) / (length l)

sommme :: Int ->[Int] -> Int
sommme n (x:xs) = 
    sommme (n+x) xs


-- exercice 3

variance :: [Int] -> Double
