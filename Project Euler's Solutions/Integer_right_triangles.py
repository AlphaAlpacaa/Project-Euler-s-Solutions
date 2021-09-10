"""DİK Açılı bir üçgen olacak şekilde p üçgenin çevresiyse
hangi p değeri için çözüm sayısı maximumdur (p<1000)
örnek: p = 120 için 3 tane (20,48,52) (24,45,51) (30,40,50)"""
result = 0
number = 0
for p in range(1,1000):
    sayac= 0
    for a in range(1,999):
        for b in range(1,a):
            c = (a**2 + b**2)**0.5
            if p == a+b+c:
                sayac += 1
    if sayac > result:
        result = sayac
        number = p
print(number)


