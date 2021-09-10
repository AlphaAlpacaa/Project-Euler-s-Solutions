import time
def palindrom(number):
    if (str(number) == str(number)[::-1]):
        return True

def iki_tabanliya_cevirme(number):
    new_number = str()
    while True:
        if number == 1 or number == 0:
            new_number += str(number%2)
            break
        new_number += str(number%2)
        number //= 2
    return(new_number)[::-1]

sum = 0
for number in range(1,1000000):
    if palindrom(number) ==True:
        if palindrom(iki_tabanliya_cevirme(number)) == True:
            sum += number

print(sum)
