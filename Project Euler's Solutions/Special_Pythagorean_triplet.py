b = 1
while True:
    for a in range(1,1000):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print(a*b*c)
            break
    b += 1
    if b == 1000:
        break
