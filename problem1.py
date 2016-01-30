
def main():
    multiples_of_3 = range(0, 1000, 3)
    multiples_of_5 = range(0, 1000, 5)
    all_multiples = set(multiples_of_3 + multiples_of_5)
    result = reduce(lambda x, y: x + y, all_multiples)
    print result

if __name__ == '__main__':
    main()
