import itertools
import time

start = time.time()
numbers = [1,2,3,4,5,6,7,8,9]
permutations = list(itertools.permutations(numbers,9))

result = set()

for number in permutations:
    sayi1 = number[0]*10+number[1]
    sayi2 = number[2]*100+number[3]*10+number[4]
    sayi3 = number[5]*1000+number[6]*100+number[7]*10+number[8]
    if sayi1* sayi2 == sayi3:
        result.add(sayi3)

    number1 = number[0]
    number2 = number[1]*1000+number[2]*100+number[3]*10+number[4]
    number3 = number[5] * 1000 + number[6] * 100 + number[7] * 10 + number[8]
    if number1*number2 == number3:
        result.add(number3)
finish = time.time()
print(sum(result))
print(finish-start)