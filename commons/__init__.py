import math

def is_prime(n):
    n_sqrt = int(math.sqrt(n)) + 1
    for i in range(2, n_sqrt):
        if n % i == 0:
            return False
    return True
