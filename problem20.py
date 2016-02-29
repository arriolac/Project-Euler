def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def main():
    factorial_100 = factorial(100)
    print "100! = {}".format(factorial_100)
    summation = reduce(lambda x, y: x + y, [int(c) for c in str(factorial_100)])
    print "Sum is: {}".format(summation)


if __name__ == '__main__':
    main()
