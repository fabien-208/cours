import Prelude hiding (length)
import Data.List hiding (length)

length = genericLength



moyenne :: [Double] -> Double
moyenne [] = 0
moyenne l = (sum l) /length l


main :: IO ()
main = do
    putStrLn "Entrez une liste de note"
    saisie <- getLine
    let n = read saisie in
        print(moyenne n)