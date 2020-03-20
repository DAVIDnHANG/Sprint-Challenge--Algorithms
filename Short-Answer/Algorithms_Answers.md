#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  given a=0, while(a < n^3) { a=a+n^2}
let solve for a at a=0.
1) a = 0 + n^2
2) a = n^2 + (n^2)
3) a =  n^2 + n^2 = 2n^2
4) a = 2n^2 + n^2 = 3n^2
5) a=kn^2 such that k 1,2... an interger
when does it stop?
1) a >= n^3
2) plug in a from above
3) kn^2\n^2 >= n^3\n^2
4) k = n
5) O(n) = k
    
b)  
sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
sequence is the following:
   i  j     sum              
   0  1     0
   1  1*2=2    0+1=1 
   1  2*2=4    1+1=2     
   1  4*2=8    2+1=3
   n   2^k      k
for j >= n
    2^k >= n
    k  >= (ln_2(n) + k)
    while i in range(n)
      n(ln_2(n)+k)
```


c)c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

bunnies 
0  0
1  2 + (0)
2  2 + (2+0) + (0)
3  2 + (2+0) + (2+0) 
k  2 + k(2) = k2
O(n)



## Exercise II

go on floor 1, toss egg if egg does not breaks then move up a floor.
go on floor 2, toss egg, if egg does not break then move up a floor.
go on floor 3, toss egg, if egg breaks, stop moving up floor.
 
for f in story building:
   if egg does not break, 
       ++f.
   if egg does break
      egg break at this floor.

for f in story building:
  while(n > F )
    go to half way
       if egg break then, go half way down floor.
       if egg does not break, go half way up floor.
