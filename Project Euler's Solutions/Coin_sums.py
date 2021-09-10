"""
a = 1p
b = 2p
c = 5p
d = 10p
e = 20p
f = 50p
g = 100p
h = 200p"""

counter = 0

for x in range(2):
    for a in range(3):
        if 200 * x + 100 * a > 200:
            break
        for b in range(5):
            if 200 * x + 100 * a + b * 50> 200:
                break
            for c in range(11):
                if 200 * x + 100 * a + b * 50 + 20 * c> 200:
                    break
                for d in range(21):
                    if 200 * x + 100 * a + b * 50 + c * 20 + d * 10> 200:
                        break
                    for e in range(41):
                        if 200 * x + 100 * a + b * 50 + c * 20 + d * 10 + 5 *e> 200:
                            break
                        for f in range(101):
                            if 200 * x + 100 * a + b * 50 + c * 20 + d * 10 + 5 * e + 2 *f <= 200:
                                counter+= 1
print(counter)




