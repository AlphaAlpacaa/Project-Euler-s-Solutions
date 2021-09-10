"""sayi = 13463467
while True:
    sayi //= 10
    print(sayi)
    if sayi < 3:
        break"""
liste=list()

for number in range(2,1000000):
    number = str(number)
    toplam = 0
    for i in number:
        i = int(i)
        toplam += i**5
    if toplam == int(number):
        liste.append(int(number))
sum = 0
print(liste)
for i in liste:
    sum += i
print(sum)