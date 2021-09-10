"""It was proposed by Christian Goldbach
that every odd composite number can be written
as the sum of a prime and twice a square.
9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12
It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the
 sum of a prime and twice a square?"""

from sympy import isprime
number = 9
while True:
    if isprime(number) or number%2 == 0:
        number+= 1
        continue
    sayac = False
    n = 1
    while number-2*n*n > 0:
        if isprime(number-2*n*n):
            sayac = True
            break
        n += 1
    if not sayac:
        print(number)
        break
    number+=1