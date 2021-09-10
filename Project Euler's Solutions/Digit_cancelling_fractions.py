def associate_number(number1,number2):
    number1 = str(number1)
    number2 = str(number2)
    if number1[0] == number2[0] or number1[0] == number2[1] or number1[1] == number2[0] or number1[1] == number2[1]:
        return True

def delete_associate_number(number1,number2):
    number1 = str(number1)
    number2 = str(number2)
    if number1[0] == number2[0]:
        number1 = number1[1]
        number2 = number2[1]
    elif  number1[0] == number2[1]:
        number1 = number1[1]
        number2 = number2[0]*10
    elif number1[1] == number2[0]:
        number1 = number1[0]*10
        number2 = number2[1]
    elif number1[1] == number2[1]:
        number1 = number1[0] * 10
        number2 = number2[0] * 10

liste_pay = []
liste_payda = []

for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                number1 = 10 * a + b
                number2 = 10 * c + d
                if number2 > number1:
                    original_number1 = number1
                    original_number2 = number2
                    if associate_number(number1,number2) == True:
                        delete_associate_number(number1,number2)
                        if int(number1)/int(number2) == int(original_number1)/int(original_number2):
                            liste_pay.append(number1)
                            liste_payda.append(number2)


print("paydalar:",liste_pay)
print("paydalar:",liste_payda)