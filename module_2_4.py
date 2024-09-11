# Пухаева Алина Александровна
# The for loop.
# 11.09.2024
# Notes: ctrl+alt+L
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for n_ in numbers:
    if n_ == 1:
        continue
    is_prime = True
    for i in range(2, int(n_ ** 0.5) + 1):
        if n_ % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(n_)
    else:
        not_primes.append(n_)
print("Primes:", primes)
print("Not Primes:", not_primes)