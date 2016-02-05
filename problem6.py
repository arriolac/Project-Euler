import math

def main(n):
    print square_of_sum(n) - sum_of_squares(n)

def sum_of_squares(n):
    squares = [int(math.pow(i, 2)) for i in range(1, n+1)]
    return reduce(lambda x, y: x + y, squares)

def square_of_sum(n):
    summation = (n + 1) * (n / 2)
    return int(math.pow(summation, 2))

if __name__ == '__main__':
    main(100)
