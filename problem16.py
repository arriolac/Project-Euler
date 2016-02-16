import math

def main():
    result = int(math.pow(2, 1000))
    result_arr = [int(digit) for digit in str(result)]
    return reduce(lambda x, y: x+y, result_arr)

if __name__ == '__main__':
    print main()
