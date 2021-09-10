"""Triangle, pentagonal, and hexagonal numbers are generated
by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and
 hexagonal."""

def triangle(n):
    return ((n*(n+1))/2)

def pentagonal(n):
    return (n*((3*n)-1)/2)

def hexagonal(n):
    return (n*((2*n)-1))
triangle_list = []
pentagonal_list = []
hexagonal_list = []
for n in range(144,100000):
    triangle_list.append(triangle(n))
    pentagonal_list.append(pentagonal(n))
    hexagonal_list.append(hexagonal(n))

for i in hexagonal_list:
    if i in pentagonal_list:
        if i in triangle_list:
            print(i)
            break

