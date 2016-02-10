from commons import is_prime

def main():
    acc = 2
    for i in range(3, 2000000, 2):
        if is_prime(i):
            acc += i
    print acc

if __name__ == '__main__':
    main()
