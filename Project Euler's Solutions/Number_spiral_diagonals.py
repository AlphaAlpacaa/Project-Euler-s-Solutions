a = 1
sayac = 1
liste = list()
liste.append(a)
b = 2
while sayac < 2001:
    a = a + b
    liste.append(a)
    a = a + b
    liste.append(a)
    a = a + b
    liste.append(a)
    a = a + b
    liste.append(a)
    b += 2
    sayac += 4
toplam = 0
print(liste)
for i in liste:
    toplam += i
print(toplam)