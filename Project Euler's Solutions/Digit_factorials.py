from math import factorial
upper_limit = 7*factorial(9)

sum = 0
for number in range(3, upper_limit):
    ara_toplam = 0
    gecici_Sayi = number

    while gecici_Sayi != 0:
        basamak = gecici_Sayi % 10
        ara_toplam += factorial(basamak)
        gecici_Sayi //= 10
    if ara_toplam == number:
        sum += number
        print(number)
print(sum)



