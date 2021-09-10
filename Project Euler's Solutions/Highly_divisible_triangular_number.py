import math
def bolensayi(x):
    bolen = 1
    for i in range(2,int(math.sqrt(x) + 1)):
        if x % i == 0:
            bolen +=1
        return bolen *2
n = 1
while True:
    number = (n*(n+1))/2
    if bolensayi(number > 500):
        print(number)
        break
    n += 1

