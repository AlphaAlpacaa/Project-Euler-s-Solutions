"""Beşgen sayılar, Pn = n (3n − 1) / 2 formülü ile üretilir.
 İlk on beşgen sayı:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

P4 + P7 = 22 + 70 = 92 = P8 olduğu görülebilir.
 Ancak, 70 - 22 = 48 arasındaki fark beşgen değildir.

Toplamları ve farkları beşgen ve D = | Pk - Pj |
 olan beşgen sayı çiftini bulun, Pj ve Pk | en küçük;
  D'nin değeri nedir?"""

def pentagonal_number(n):
    return (n*(3*n-1))/2
def is_pentagonal(x):
    return ((1 + (1 + 24 * x)**(1/2)) / 6).is_integer()

for i in range(1,5000):
    number1 = pentagonal_number(i)
    for j in range(i-1,0,-1):
        number2 = pentagonal_number(j)
        if is_pentagonal(number1 + number2) and is_pentagonal(number1-number2) == True:
            print(number1-number2)
