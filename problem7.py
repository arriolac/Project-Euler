from commons import is_prime

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
