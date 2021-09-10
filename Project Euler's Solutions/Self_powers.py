"""The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000."""
result = 0
for a in range(1,1000):
    result += a**a
result = str(result)[::-1]
print(result[0:10])