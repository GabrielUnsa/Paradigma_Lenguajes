fact1 :: Integer -> Integer
fact1 n = if n==0
		  then 1
		  else n * fact1(n-1)

cDivisores :: Int-> Int
cDivisores a = length (divisores a)

listaDivisores :: [Int]-> [Int]
listaDivisores lista | lista==[] = []
listaDivisores (x:xs)= cDivisores x : listaDivisores xs

horner :: (Num a)=>a ->[a] -> a
horner x = foldr (\a b -> a + b*x) 0

devolver :: Integer -> [a]-> [a]
devolver n _ | n<=0 = []
devolver n []=[]
devolver n (x:xs)= x : devolver (n-1) xs

swap :: (x,y)-> (y, x)
swap (x,y)= (y,x)

apply :: x -> x
apply x = x

first :: (Int,Int)-> Int
first (x,y) = x

sign :: Int -> String
sign x | x>0  = "Positivo"
	   | x == 0 = "Cero"
	   | otherwise = "Negativo"


abs :: Integer -> Integer
abs x = if x>0
		  then x
		  else -x

pot :: (Num x) => x -> Int -> x
pot x y = if y==0
		  then 1
		  else x * pot x (y-1)

xor :: Bool -> Bool -> Bool
xor x y = (x && y)

max3 :: Int -> Int -> Int -> Int
max3 x y z = (succ(max x (max y z))-1)

longitud :: [Int] -> Int
longitud lista = length lista

producto:: (Num x)=> x -> Int -> x
producto x y = if y==0
			   then 0
			   else x + producto x (y-1)

radio :: Float -> Float
radio x = x*x*pi

concatenaLista :: [Int]-> [Int]-> [Int]
concatenaLista lista1 lista2 = lista1++lista2

productoLista :: (Num x)=> [x]-> x
productoLista [] = 1
productoLista (x:xs) =  x*productoLista xs

productoEscalar :: (Num x)=> [x]-> [x]-> x
productoEscalar xs ys = sum [x*y | (x,y) <- zip xs ys]

eliminaPares :: [Int]-> [Int]
eliminaPares lista = [x | x <- lista , x `mod` 2 == 1]

concatenaListas ::(Num x)=> [[x]]-> [x]
concatenaListas [ ]=[]
concatenaListas (x:xs)= x ++ concatenaListas xs

factores :: Int -> [Int]
factores n = [x | x <- [1..n], n `mod` x == 0]

perfectos :: Int -> [Int]
perfectos n = [x | x <- [1..n], sum (init (factores x)) == x]

divideAB :: Int -> Int-> Bool
divideAB x y | (y `mod` x)==0 = True
			 | otherwise = False

divisores :: Int-> [Int]
divisores a = [x | x <- [1..a], a `mod` x == 0]

revertirLista :: [Char]-> [Char]
revertirLista lista = reverse lista

palindromo :: [Char]-> Bool
palindromo lista= if reverse lista == lista then True
				  else False

mul26 :: [Integer]-> [Integer]
mul26 lista = [x | x <- lista, x `mod` 2 == 0, x `mod` 6 /= 0]

drowLista :: [Int]-> Int-> [Int]
drowLista lista y | y<0 = []
drowLista [] y = []
drowLista lista y = take y lista ++ drowLista (drop (y+1) lista) y

adyasentes :: [Int]->[(Int,Int)]
adyasentes [] = []
adyasentes lista = [ (head lista,head(tail lista)) ] ++ adyasentes (drop 1 lista)

incrementa :: [Int]-> Int-> [Int]
incrementa [] _ = []
incrementa (x:xs) a = x+a : incrementa xs a

incrementa2 :: [Int]-> Int-> [Int]
incrementa2 lista a = map(a+) lista

sumar :: [Int]-> Int
sumar lista = foldr(+) 0 lista

takeLista :: Integer -> [a]-> [a]
takeLista n lista = devolver n (reverse lista)

euclides :: Int-> Int-> Int
euclides a b
				| b==0 =a
				| otherwise = euclides b (a `mod` b)


m::Integer->Integer->Integer->Integer
m a b x |a==b = a
		     |rem (a*x) b==0 = (a*x)
		     |otherwise = m a b (x+1)

mcm::Integer->Integer->Integer
mcm a b = m a b 1

reverInt :: Int-> Int
reverInt x = rever x 0

rever:: Int-> Int-> Int
rever x y | x==0 = y
rever x y | x>0 = rever (x`div`10) (10*y + x`mod`10 )

vecInt :: Int-> [Int]
vecInt x | x==0 = []
vecInt x | x>0 = [x `mod` 10] ++ vecInt (x `div` 10)

vec2Int :: Int-> [Int]
vec2Int x = vecInt (reverInt x)

primo :: Int->Bool
primo x | (length(divisores x))==2 = True
		| otherwise = False

qsort :: Ord a => [a] -> [a]
qsort [] = []
qsort (p:xs) = qsort menor ++ [p] ++ qsort mayor
    where
        menor = [ y | y <- xs, y < p ]
        mayor = [ y | y <- xs, y >= p ]

vecPrimo :: Int-> [Int]
vecPrimo n = prim n 2

prim :: Int-> Int-> [Int]
prim n _ | n==0 = []
prim n x = if(primo x == True ) then [x] ++ prim (n-1) (x+1)
					 else [] ++ prim n (x+1)

busSec::Ord a=>[a]->a->Bool
busSec [] _ = False
busSec (x:xs) ele
	| x==ele = True
	| True = busSec xs ele

foo :: (a->a)->a->a
foo x y = x (x y)

repead :: Int->[Char]->[Char]
repead n cadena | n==0 = ""
repead n cadena = cadena ++ repead (n-1) cadena

alternaParImpar :: [Int]-> [Int]
alternaParImpar lista = parImpar (par lista) (impar lista)

par :: [Int]->[Int]
par [] = []
par lis = [ x | x <- lis, even x == True]

impar :: [Int]->[Int]
impar [] = []
impar lis = [ x | x <- lis, odd x == True]

parImpar :: [Int]->[Int]->[Int]
parImpar [] [] =[]
parImpar (x:xs) (y:ys) = [x,y] ++ parImpar xs ys
