liste = []
yeni_liste = []
for a in range(2,10):
    liste.append(str(a))
    while True:
        if a % 2 == 0:
            a = a//2
            liste.append(str(a))
        else:
            a = 3*a+1
            liste.append(str(a))
        if a == 1:
            break
    if len(liste)>len(yeni_liste):
        liste = yeni_liste
yeni_liste = ",".join(yeni_liste)
print(max(yeni_liste.split("1")))

