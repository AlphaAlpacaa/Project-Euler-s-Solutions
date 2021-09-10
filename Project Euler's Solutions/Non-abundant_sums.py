liste = []
def abundantNumber(x):
    sum = 0
    for i in range(1,x//2+1):
        if x % i == 0:
            sum += i
    if sum > x:
        liste.append(x)
        return x
for i in range(1,28124):
    abundantNumber(i)
ikiliToplam = []
for a in liste:
    for b in liste:
        if a != b:
            ikiliToplam.append(a+b)
NumberList = list()

for b in range(1,28123):
    NumberList.append(b)
kumeIkiliToplam = set(ikiliToplam)
kumeNumberList = set(NumberList)
print(liste)
print(kumeIkiliToplam)
toplam= 0
for c in (kumeNumberList.difference(kumeIkiliToplam)):
    toplam+=c
    print(c)
print(toplam-64)