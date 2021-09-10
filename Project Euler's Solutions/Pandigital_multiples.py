#herhangi bir sayıyı 1 2 3 N e kadar sayılarıyla çarpıp(9basamaklı
#sayı elde edene kadar arka arkaya
#koyduğunda pandigital(1den 9 a tüm rakamları birer kez içeren) oluyorsa
#bunları listeye al en büyüğü söyle.

liste = []
def pandigital_Controller(number):
    if "1" in str(number):
        if "2" in str(number):
            if "3" in str(number):
                if "4" in str(number):
                    if "5" in str(number):
                        if "6" in str(number):
                            if "7" in str(number):
                                if "8" in str(number):
                                    if "9" in str(number):
                                        liste.append(number)

a = 2
check_list = []
for number in range(1,10000):
    if len(str(number)+str(number*2)) >= 9:
        if len(str(number)+str(number*2)) == 9:
            check_list.append(str(number)+str(number*2))
    elif len(str(number)+str(number*2) + str(number*3)) >= 9:
        if len(str(number) + str(number * 2) + str(number * 3)) == 9:
            check_list.append(str(number) + str(number * 2) + str(number * 3))
    elif len(str(number)+str(number*2) + str(number*3) + str(number*4)) >= 9:
        if len(str(number) + str(number * 2) + str(number * 3) + str(number * 4)) == 9:
            check_list.append(str(number)+str(number*2) + str(number*3) + str(number*4))
for i in check_list:
    if pandigital_Controller(i) == True:
        liste.append(i)
print(max(liste))