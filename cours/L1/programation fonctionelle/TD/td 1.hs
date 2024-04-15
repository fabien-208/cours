"exercice 4"

abs :: Int -> Int
abs x = 
    if x > 0
        then x
        else x * -1


max :: Int -> Int -> Int
max x y =
    if x > y
        then x
        else y


second2 :: [Int] -> Int
second2 x =
    if (lenght x) > 2
        then x!!2
        else -1

    
moyenne3 :: [int] -> Double
moyenne3 l =
    if (length l) > 0
        then moyenne2 l
        else -1


max3 :: Int -> Int -> Int -> Int
max3 x y z =
    if x > y
        then (max x z)
        else (max y z) 


jugement2 :: [int] -> Char
jugement2 [] = "Absent"
jugement2 l =
    moy = (sum l) / (length l)
    if moy < 10
        then "Absent"
        else if moy < 15
            then "Pas mal"
            else "Bravo champion"


Est_vide :: [a] -> Bool
Est_vide l = 
    if (length l) = 0
        then True
        else False



"exercice 5"


maxList :: [Int] -> Int
maxList l = maxList' l (l!!0)

maxList' :: Int -> Int -> Int
maxList' [] res = res
maxList' (x;xs) res =
    if x > res
        then maxList' xs (l!!i)
        else maxList' xs res



maxList2 :: [Int]
maxList2 [] = -1
maxList2 l =
    maxList l
