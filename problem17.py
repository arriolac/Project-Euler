from num2words import num2words

def main():
    acc = 0
    for i in range(1, 1001):
        s = strip(num2words(i))
        acc += len(s)
    return acc

def strip(s):
    s = s.replace(" ", "")
    return s.replace("-", "")

if __name__ == '__main__':
    print main()
