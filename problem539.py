from datetime import datetime

RIGHT = 0
LEFT = 1

def reduce_array(array, direction):
    array_length = len(array)
    iter_array = range(0, array_length) if direction == LEFT else range(-array_length, 0)
    return [
        array[i]
        for i in iter_array
        if i % 2 == direction
    ]

def foo(n):
    #array = range(1, n+1)
    #direction = LEFT
    array = range(2, n+1, 2)
    direction = RIGHT
    while len(array) != 1:
        array = reduce_array(array, direction)
        direction = (LEFT if direction == RIGHT else RIGHT)
        print array
    return array[0]

def bar(n):
    acc = 1  # since foo(1) == 1
    for i in range(2, n+1, 2):
        acc += 2 * foo(i)
    return acc

def log_time():
    print unicode(datetime.now())

if __name__ == '__main__':
    log_time()
    print bar(100)
    log_time()
