import sympy
prime_count = 0

for a in range(-999,1000):
    for b in sympy.primerange(1,1000):
        aux_prime_count = 0
        n = 0
        while sympy.isprime(n **2 + a*n + b):
            aux_prime_count += 1
            n += 1
        if aux_prime_count > prime_count:
            prime_count = aux_prime_count
            a_max = a
            b_max = b
print(a_max*b_max)
print(prime_count)
