"""1406357289 sayısı, 0'dan 9'a kadar olan bir pandigital sayıdır
çünkü 0'dan 9'a kadar olan rakamların her birinden bir sırayla
oluşur, ancak aynı zamanda oldukça ilginç bir alt dizge
 bölünebilme özelliğine de sahiptir.

D1 1. hane, d2 2. hane olsun, vb. Bu şekilde aşağıdakilere
 dikkat ediyoruz:

d2d3d4 = 406, 2'ye bölünebilir
d3d4d5 = 063, 3'e bölünebilir
d4d5d6 = 635, 5'e bölünebilir
d5d6d7 = 357, 7'ye bölünebilir
d6d7d8 = 572, 11'e bölünebilir
d7d8d9 = 728, 13'e bölünebilir
d8d9d10 = 289, 17'ye bölünebilir
Bu özelliğe sahip tüm 0 ila 9 pandigital sayıların toplamını bulun.
"""
from itertools import permutations

digits = "0123456789"
numbers = permutations(digits)
numberList = ["".join(number) for number in numbers if not number[0]== "0"]
sum_ = 0
primes =[2,3,5,7,11,13,17]
for number in numberList:
    is_okay = True
    for i in range(7):
        if int(number[i+1:i+4]) % primes[i] != 0:
            is_okay = False
            break
    if is_okay:
        sum_ += int(number)
print(sum_)


