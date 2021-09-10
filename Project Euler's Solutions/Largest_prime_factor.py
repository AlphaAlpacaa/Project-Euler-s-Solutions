liste = []
liste2 = []
sayac = 0
for j in range(3,550):
    sayac = 0
    for i in range(2,j):
        if(j % i == 0):
            sayac += 1
    if sayac == 0:
        liste.append(j)
if (550 % 2 == 0):
    liste2.append(2)
for a in liste:
    if (550 % a == 0):
        liste2.append(a)
print(max(liste2))



