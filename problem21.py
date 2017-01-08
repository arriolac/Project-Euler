import math

def sum_divisors(n):
    total = 1
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            total += i
            total += (n/i)
    return total

def main():
    pairs = set()
    for a in range(1, 10000):
        if a not in pairs:
            b = sum_divisors(a)
            if a != b and a == sum_divisors(b):
                pairs.add(a)
                pairs.add(b)

    sum = 0
    for num in pairs:
        sum += num
    print sum

if __name__ == '__main__':
    main()
