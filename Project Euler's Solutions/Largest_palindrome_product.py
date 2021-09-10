a = 999
liste = list()
while True:
    for i in range(100,999):
        if(str(a * i) == str(a * i) [::-1]):
            liste.append(a * i)
    a -= 1
    if a == 0:
        break
print(liste)




