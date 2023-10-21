# پیدا کردن اعداد اول دو قلو

n = 1000

prime_numbers = [2]
for i in range(3, n+1, 2):

    for p in prime_numbers:
        if i % p == 0:
            break
    else:
        prime_numbers.append(i)

twin_prime_numbers = []

for p in prime_numbers:
    if p and p+2 in prime_numbers:
        twin_prime_numbers.append((p, p+2))
     
# print(prime_numbers)

# print(len(prime_numbers))

print(twin_prime_numbers)

print(len(twin_prime_numbers))

