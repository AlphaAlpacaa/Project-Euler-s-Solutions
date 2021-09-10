"""
123456789101112131415161718192021...
sayısının 1 10 100 1000 10000 100000 ve 1 milyonuncu
rakamlarının çarpımı kaçtır?
"""
number = ""
addition = 1
while len(number) <= 1000000:
    number += str(addition)
    addition += 1
print(int(number[0])*int(number[9])*int(number[99])*int(number[999])*int(number[9999])*int(number[99999])*int(number[999999]))