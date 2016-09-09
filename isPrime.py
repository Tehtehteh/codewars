from math import sqrt, ceil
def is_prime(num):
    for i in range(2,ceil(sqrt(num))):
        if num % i == 0:
            print(i)
            return False
    return True

print(is_prime(19))