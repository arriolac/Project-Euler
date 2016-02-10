import math

def main():
    for a in range(998, 0, -1):
        diff = 1000 - a
        for j in range(2, diff):
            b = j
            c = diff - j
            if math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2):
                print "a: {}, b: {}, c: {}".format(a, b, c)
                return a * b * c

if __name__ == '__main__':
    print main()
