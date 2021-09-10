liste1 = []
liste2 = []

a = 1
for i in range(1,20):
    if 2**a == i :
        liste1.append(2**a)
        a += 1
a = 1
for i in range(1,20):
    if 3**a == i :
        liste2.append(3**a)
        a += 1
print(5*7*11*13*17*19*max(liste1)*max(liste2))