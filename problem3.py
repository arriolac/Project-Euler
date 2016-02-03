import math

def main(n):
    factors = []
    n_sqrt = int(math.sqrt(n)) + 1
    for i in range(2, n_sqrt):
        if n % i == 0:
            factors.append(i)
    all_factors = [] + factors
    for i in factors:
        all_factors.append(n /i)

    max_prime_factor = 0
    for factor in all_factors:
        if is_prime(factor) and factor > max_prime_factor:
            max_prime_factor = factor
    print max_prime_factor

def is_prime(n):
    n_sqrt = int(math.sqrt(n)) + 1
    for i in range(2, n_sqrt):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = 600851475143
    main(n)
