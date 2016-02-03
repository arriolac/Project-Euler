fib_memoized = [0, 1]

def fib(x):
    if x < len(fib_memoized):
        return fib_memoized[x]
    else:
        val = fib(x-1) + fib(x-2)
        fib_memoized.append(val)
        return fib_memoized[-1]

if __name__ == '__main__':
    acc = 0
    x = 0
    fib_val = fib(0)
    while fib_val < 4000000:
        fib_val = fib(x)
        if fib_val % 2 == 0:
            acc += fib_val
        x+=1
    print acc
