"""pandigital olan en büyük asal sayı kaçtır?(padigital 1 den n e kadar
bütün rakamları 1 kez içeren)
9 veya 8 basamaklı olsaydı  3 e bölünür sayımız en fazla 7 basamaklı olacak."""
liste = []
def pandigital_Controller(number):
    if "1" in str(number):
        if "2" in str(number):
            if "3" in str(number):
                if "4" in str(number):
                    if "5" in str(number):
                        if "6" in str(number):
                            if "7" in str(number):
                                liste.append(number)

def prime_Number(number):
    sayac = 0
    for i in range(2,number):
        if(number % i == 0):
            sayac += 1
    if sayac == 0:
        return True

for number in range(7000000,8000000):
    pandigital_Controller(number)

result_List = []
for number in liste:
    if prime_Number(number) == True:
        result_List.append(number)
print(max(result_List))