import sympy

def truncatable_left(number):
    sayi = str(number)
    flag = True
    for i in range(len(sayi)):
        sayi2 = int(sayi[i::])
        if sympy.isprime(sayi2) == False:
            flag = False
    return flag

def truncatable_right(number):
    sayi = str(number)
    flag = True
    for i in range(len(sayi)):
        sayi2 = int(sayi[:i+1:])
        if sympy.isprime(sayi2) == False:
            flag = False
    return flag

truncated_count = 0
try_number = 10
truncated_numbers = []
while True:
    if sympy.isprime(try_number) and truncatable_right(try_number) and truncatable_left(try_number):
        truncated_numbers.append(try_number)
        truncated_count += 1
    try_number += 1
    if truncated_count == 11:
        break
sum = 0
for i in truncated_numbers:
    sum += i
print(sum)