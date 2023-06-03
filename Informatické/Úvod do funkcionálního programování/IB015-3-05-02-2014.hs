-- /* IB015 - 3.termín - Podzim 2013 - 5.2.2014 - súbor je možné načítať do interpretra haskell, po zakomentovaní haskell kódu a odkomentovní prolog kódu je možné načítať aj prologový kód

-- Zapíš intenzionálne zoznam možných dĺžok strán pravouhlého trojuholníka (A, B, C) - platí, že A^2 = B^2 + C^2
triangles = [ (a, b, c) | a <- [1..]
                        , b <- [1..a]
                        , c <- [1..a]
                        , a^2 == b^2 + c^2 ]

complexity n = map (replicate n) (replicate (n*n) 1)
--  zložitosť výrazu je kubická -> n * n^2 = n^3


data Armada = Vojak | Velitel [Armada] deriving (Show)
-- typový konštruktor: Armada
-- dátový konštruktor: Vojak
-- dátový konštruktor: Velitel
-- Napíš hodnotu typu Armada, ktorá bude používať aspoň jeden krát konštruktor Vojak a Velitel
hodnota = Velitel [Vojak]

-- Napíš funkciu posila, ktorá každému velitelovi priradí navyše jedného Vojak-a
posila :: Armada -> Armada
posila (Velitel as) = Velitel $ 
                      Vojak : map posila as
posila Vojak        = Vojak


-- preveď do pointfree
f = error "neviem už, čo to bolo"
-- */

{-
% Napíšte funkciu suma, ktorá sčíta všetky prvky zoznamu
suma([], 0).
suma([H | T], R) :- suma(T, S), R is S + H.

% prípadne pomocou akumulátora
sumaA([], A, A).
sumaA([H | T], A, R) :- B is A - H, sumaA(T, B, R).
% suma(L, R) :- sumaA(L, 0, R).

% Nakreslite výpočtový strom vyhodnotenia dotazu ?- a(X). nad databázou faktov

a(X) :- b(X).
a(1).

b(2).
b(4).
b(X) :- c(X, _Y), ! .

c(2, 1).
c(3, 1).

/*                                        +----------+
                                          | ?- a(X). |
                                          +---+---+--+
                                              |   |
                                              |   |
                               +---------+    |   |    +---------+
                               |[ a(X). ]|    |   |    |[ a(1). ]|
                               |         |<---+   +--->|         |
                               |  X = G1 |             |  X = 1  |
                               +---------+             +----+----+
                               |  a(G1). |                  |
                               +-----+---+                  |
                                     |                 .....+.....
                                     |                 .  X = 1  .
               +-----------------+   |                 ...........
               |[ a(X) :- b(X). ]|   |
               |                 |<--+
               |  X = G1         |                  
               +-----------------+                   
               |      b(G1).     |
               ++-------+-------++
                |       |       |
                |       v       |
+---------+     |  +---------+  |    +------------------------+
|[ b(2). ]|     |  |[ b(4). ]|  |    |[ b(X) :- c(X, Y), ! . ]|
|         |<----+  |         |  +--->|                        |
|  G1 = 2 |        |  G1 = 4 |       |  X = G1                |
+----+----+        +----+----+       |  Y = G2                |
     |                  |            +------------------------+
     |                  |            |      c(G1, G2), ! .    |
.....+.....        .....+.....       +------------+-----+-----+
.  X = 2  .        .  X = 4  .                    |     |
...........        ...........                    |     |
                                 +------------+   |     |
                                 |[ c(2, 1). ]|   |     |
                                 |            |<--+     +-->! (cut)
                                 |  G1 = 2    |
                                 |  G2 = 1    |
                                 +------------+
                                 |     ! .    |
                                 +-----+------+
                                       |
                                       |
                                  .....+.....
                                  .  X = 2  .
                                  ...........

*/
-}

