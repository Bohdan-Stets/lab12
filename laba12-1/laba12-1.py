def is_prime(n, divisor=2):
    if n < 2:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor + 1)

n = int(input("Введіть натуральне число: "))
if is_prime(n):
    print(f"{n} є простим числом")
else:
    print(f"{n} не є простим числом")
