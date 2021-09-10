karetoplam = 0
toplam = 0
for a in range(1,101):
    karetoplam += a**2
for b in range(1,101):
    toplam += b
toplam = toplam**2
print(toplam - karetoplam)
