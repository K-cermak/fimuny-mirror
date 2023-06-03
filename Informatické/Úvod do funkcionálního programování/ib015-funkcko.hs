-- Zopar prikladov ktore som dal dokopy a nechcel som ich proste vymazat, kedze som dost z nich robil ja tak za spravnost velmi nerucim, nieto este za efektivitu
-- Ak by ste nasli nejaku fatalnu chybu tak piste vorcak@mail.muni.cz a mozem ju nahradit vasim riesenim
-- Vacsinu som sa snazil zdokumentovat ale to som robil az prilis neskoro po skuske takze o niektorych veciach som proste nemal sancu, ... a ani chut to nejako velmi riesit ;)
-- Nech sa na skuske dari, hadam to aspon trocha pomoze

module Main where              
import Char
            
-- definicia binarneho stromu
data BinTree a = Empty | Node a (BinTree a) (BinTree a)
  deriving (Eq,Show)

-- priklad binarneho stromu
--        4
--     2     7
--   0   3     9

tn :: BinTree Int
tn = Node 4 (Node 2 (Node 0 Empty Empty) (Node 3 Empty Empty)) (Node 7 Empty (Node 9 Empty Empty))

--        a
--     c     b

tc :: BinTree Char
tc = Node 'a' (Node 'c' Empty Empty) (Node 'b' Empty Empty)

-- velkost binarneho stromu
size :: BinTree a -> Int
size Empty = 0
size (Node a b c) = 1 + size (b) + size(c)

-- funkcia na prechadzanie stromu
tfold :: (a->b->b->b) -> b -> BinTree a -> b
tfold _ u Empty = u
tfold g u (Node v l r) = g v (tfold g u l) (tfold g u r)

-- rekurzivny datovy typ
data Nat = Zero | Succ Nat  deriving Show
-- prevod na int, napriklad nattoint (Succ (Succ Zero)) -->* 2, Succ Zero -->* 1
nattoint :: Nat -> Int 
nattoint Zero = 0
nattoint (Succ n) = 1 + nattoint n

-- nekonecny pascalov trojuholnik
pt :: [[Integer]]
pt = iterate (\ r -> zipWith (+) ([0]++r) (r++[0])) [1]

-- tu som mal nejake pokusy o pochopenie "bodiek", asi tu toho moc neokomentujem
h,k :: (a -> a) -> a -> a
h f = f . f . f
k f = f . f

-- nasleduje par veci o ktorych trocha netusim naco som ich pisal 
nd :: Eq a => [a] -> [a]
nd [] = []
nd [x] = [x]
nd (x:y:s) = if (x==y) then (nd (y:s)) else x:(nd (y:s))

                                            
--main :: IO()
--main = do g <- getLine
--          putStr (filter isAlpha g) 

--main :: [Char] -> IO Bool
--main ahoj = do putStr (ahoj++"\n")
--               g<-getLine
--              return (g == "ano")         

main :: String -> IO ()
main s = putStr s >> getLine >>= putStr . show . (=="ano") >> putStr s                                         
        
longer :: Int -> [[a]] -> Int
longer _ [] = 0
longer n (x:s) = if (length x > n) then (1 + longer n s) else (longer n s)
       
        
-- ak sa spravne pamatam a vidim tak precita nazov 1. suboru, nazov 2. suboru ako 2hy argument a prvy subor prekopiruje do 2heho
citaj = do  i  <- getLine
            o <- getLine
            s <- readFile i 
            writeFile o s 

foldt :: (a -> b -> b -> b) -> b -> BinTree a -> b
foldt g u Empty = u
foldt g u (Node v l r) = g v (foldt g u l) (foldt g u r)

-- parnost/neparnost rekurz. typu
oddn :: Nat -> Bool
oddn Zero = False
oddn (Succ Zero) = True
oddn (Succ (Succ n)) = oddn (Succ n)

-- nekonecny zoznam neparnych cisiel od cisla zadaneho - napr. Main> take 2 (oddnats Zero) -->* [Succ Zero,Succ (Succ (Succ Zero))]
oddnats n = iterate (Succ . Succ) (if oddn n then n else Succ n)

-- vezme 2 zoznamy (Eq) a z prveho zoznamu odstrani vsetky prvky ktore su aj v druhom zozname
la :: Eq a => [a] -> [a] -> [a]
[] `la` _ = []
(a:b) `la` c = if (notElem a c) then (a : (b `la` c)) else (b `la` c) 

-- vraci ci je matica stvorcova alebo nie, ctvmat [[[3],[3]],[[3],[4]]] -->* True
ctvmat :: [[a]] -> Bool
ctvmat a = notElem False [length a == length i | i <- a]

-- diagonala matice
diagonala :: [[a]] -> [a]
diagonala s = zipWith (!!) s [0..]


slice :: Int -> [a] -> [[a]] 
slice _ [] = []
slice n s = (take n s) : slice n (drop n s)


-- fibonacciho posloupnost - pokus o vyber prvku fibonacciho posloupnosti trocha neefektivnejsie 
f 1 = 1
f 2 = 2
f n = f(n-1) + f(n-2)

fib 0 = [1]
fib n = fib (n-1) ++ (f n-2):[] 