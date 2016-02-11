import math

def num_divisors(n):
    total = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            total += 2  # Since both i and n/i are divisors
    return total

def main():
    start_n = int(math.pow(500, 2))
    triangular_num = 0
    i = 1
    while True:
        triangular_num += i
        result = num_divisors(triangular_num)
        print "i: {}, tri: {}, num_divisors: {}".format(i, triangular_num, result)
        if result > 500:
            return result
        else:
            i += 1

if __name__ == '__main__':
    print main()
