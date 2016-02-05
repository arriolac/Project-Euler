import math

def is_prime(n):
    n_sqrt = int(math.sqrt(n)) + 1
    for i in range(2, n_sqrt):
        if n % i == 0:
            return False
    return True

def main(n):
    count = 0
    i = 1
    while count != n:
        i += 1
        if is_prime(i):
            count += 1
    return i

if __name__ == '__main__':
    print main(10001)
