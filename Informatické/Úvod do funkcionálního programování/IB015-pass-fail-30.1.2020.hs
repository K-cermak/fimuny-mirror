-- Zadani PASS/FAIL 30.1.2020
-- 1.
-- napis funkci, ktera zvetsi prvky v seznamu o hodnotu druheho prvku seznamu
-- seznam ma alespon 5 prvku
f :: [Int] -> [Int]
f lst = map (+secondItem) lst
    where
        secondItem = head (tail lst)

-- 2.
-- urci typ lambda funkce
lambda :: (Int,b) -> c -> [a] -> [a]
lambda = (\x y -> take (fst x))

-- 3.
-- zadani: x je soucet y a z, alespon jeden prvek z trojice (x,y,z) je lichy 
-- [(x,y,z) | x <- ...] ~>* [(2,1,1),(3,1,2),(3,2,1),(4,1,3),(4,3,1)]
-- [(x,y,z) | x <- [2,3,4], y <- [1,2,3], let z = x-y, ((x-y)>0)&&((odd x) || (odd y))]

-- 4.
data NTree a = Node a [NTree a]
               deriving (Show)
-- a) monomofni typ: NTree Int
-- b) hodnota typu z a): Node 1 []
-- c) sumTree
sumTree :: (Num a) => NTree a -> a
sumTree (Node v [])  = v
sumTree (Node v lst) = v + (sum (map sumTree lst))

-- 5.
init' :: [a] -> [a]
init' []     = error "Not defined." -- nevim jestli nutne treba zminovat
init' [x]    = []
init' (x:xs) = x : (init' xs)