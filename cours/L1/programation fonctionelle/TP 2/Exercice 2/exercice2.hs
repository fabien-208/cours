import Prelude hiding (length)
import Data.List hiding (length)
length = genericLength


main :: IO ()
main = do
    putStrLn "Entrez une liste d entier"
    saisie <- getLine -- saisit une chaîne au clavier
    print(saisie)