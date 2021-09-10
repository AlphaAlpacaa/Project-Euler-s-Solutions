max_devir = 0
bolen = 2

while bolen < 1000:
    bolunen = 1
    kalanlar = []
    while True:
        kalan = bolunen % bolen
        if kalan in kalanlar:
            first_index = kalanlar.index(kalan)
            last_index = len(kalanlar)
            if last_index - first_index > max_devir:
                max_devir = last_index - first_index
                sayi = bolen
            break
        bolunen = kalan * 10
        kalanlar.append(kalan)
    bolen += 1

print(max_devir)
print(sayi)
