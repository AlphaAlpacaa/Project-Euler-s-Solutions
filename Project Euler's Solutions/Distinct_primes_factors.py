"""The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19

Find the first four consecutive integers to have four distinct prime factors each.
What is the first of these numbers?"""
import time
start = time.time()
def prime_factors(x):
    i = 2
    factors = set()
    while i < x ** 0.5:
        if x % i == 0:
            factors.add(i)
            x //= i
            i -= 1
        i += 1
    return len(factors)+1

number = 2*3*5*7
while True:
    okay = True
    for i in range(4):
        if prime_factors(number + i) != 4:
            okay = False
            break
    if okay:
        print(number)
        break
    number += 1
finish = time.time()
print(finish-start)
