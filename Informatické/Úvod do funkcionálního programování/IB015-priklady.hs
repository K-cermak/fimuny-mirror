delkaS :: (Num b) => [a] -> b
delkaS sez = sum [ 1 | _<-sez ]

delkaS' :: (Num b) => [a] -> b
delkaS' [] = 0
delkaS' (x:s) = 1 + delkaS' s

fact :: (Num a) => a -> a
fact 0 = 1
fact x = x * fact (x-1)

kMoc :: (Num a) => a -> a -> a
kMoc _ 0 = 1
kMoc x 1 = x
kMoc x k = x * kMoc x (k-1)

matice = [[1..5],[6..10],[11..15],[16..20],[21..25]]

downtri :: (Num a) => [[a]] -> [[a]]
downtri = zipWith take [1..]

uptri :: (Num a) => [[a]] -> [[a]]
uptri = zipWith drop [0..]

nuldiv :: (Integral a) => a -> [a] -> [a]
nuldiv 0 _ = error "Nulou nelze delit!"
nuldiv cis sez = [x | x<-sez, x `mod` cis == 0]

rekniKolik :: Int -> [Char]
rekniKolik cis
           | cis == 1 = "Straze pusti jednicku!"
	   | cis == 2 = "Straze pusti dvojku!"
	   | cis == 3 = "Straze pusti trojku!"
	   | otherwise = "Jine cislo straze nepusti!"

posledni :: [a] -> a
posledni [] = error "Prazdne seznamy nemaji posledniho clena."
posledni [x] = x
posledni (_:s) = posledni s

ocas :: [a] -> [a]
ocas [] = error "Prazdny seznam nema ocas."
ocas [x] = error "Jednoprvkovy seznam nema ocas."
ocas (x:s) = s

predek :: [a] -> [a]
predek [] = error "Prazdny seznam nema predek."
predek [x] = []
predek (x:s) = [x] ++ (predek s)

porovnej :: (Ord a, Show a) => a -> a -> [Char]
porovnej x y
	 | x == y = "rovnaj se"
	 | x < y = show x ++ " je mensi nez " ++ show y
	 | otherwise = show x ++ " je vetsi nez " ++ show y

fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

inicialy :: [Char] -> [Char] -> [Char]
inicialy (a:_) (b:_) = [a] ++ ". " ++ [b] ++ "."

maximum' :: (Ord a) => [a] -> a
maximum' [] = error "Prazdny seznam nema maximum."
maximum' [x] = x
maximum' (x:s) = if x > maximum' s then x else maximum' s

max' :: (Ord a) => a -> a -> a
max' a b = if a>b then a else b

replicate' :: (Integral a) => a -> b -> [b]
replicate' a x = if a<=1 then [] else x : replicate' (a-1) x

take' :: Int -> [a] -> [a]
take' a _
      | a<=0 = []
take' _ [] = []
take' a (x:s) = x : take' (a-1) s

reverse' :: [a] -> [a]
reverse' [] = []
reverse' (x:s) = reverse' s ++ [x]

quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:s) = if x == minimum (x:s) then x : quicksort s else quicksort (s++[x])

zap :: Float -> Int -> Float
zap x a = 1/(x^a)

flip' :: (a -> b -> c) -> (b -> a -> c)
flip' f x y = f y x

zipWith' :: (a -> b -> c) -> [a] -> [b] -> [c]
zipWith' _ [] _ = []
zipWith' _ _ [] = []
zipWith' f (a:x) (b:y) = f a b : zipWith' f x y

zip' :: [a] -> [b] -> [(a,b)]
zip' _ [] = []
zip' [] _ = []
zip' (a:x) (b:y) = (a,b) : zip' x y

collr :: (Integral a) => a -> [a]
collr 1 = [1]
collr x
      | odd x = x:collr (x*3+1)
      | otherwise = x:collr (div x 2)

map' :: (a -> b) -> [a] -> [b]
map' f xs = foldr (\x acc -> f x:acc ) [] xs

sum' :: (Num a) => [a] -> a
sum' s = foldl (\acc x -> acc + x) 0 s

shuffle :: [a] -> [Int] -> Int -> [a]
shuffle x n p = take p (cycle (map (\a -> x !! a) n))

data Den = Po | Ut | St | Ct | Pa | So | Ne deriving (Show)

weekend :: Den -> Bool
weekend So = True
weekend Ne = True
weekend _ = False

data Nat = Zero | Succ Nat deriving (Show)

cislo :: Nat -> Int
cislo Zero = 0
cislo (Succ x) = 1 + cislo x

data Teleso = Kvadr Float Float Float -- a, b, c
            | Valec Float Float       -- r, v
            | Kuzel Float Float       -- r, v
            | Koule Float             -- r

objem :: Teleso -> Float
objem (Kvadr a b c) = a*b*c
objem (Valec r v)   = pi*r^2*v
objem (Kuzel r v)   = (1/3)*pi*r^2*v
objem (Koule r)     = (4/3)*pi*r^3

sloupce :: [[m]] -> [[m]]
sloupce [[]] = error "Nezadali jste zadnou matici."
sloupce mat = [zipWith (!!) mat [n|x<-[1..(length mat)]] | n<-[0..((length mat)-1)]]
