import math

def is_prime(n):
    n_sqrt = int(math.sqrt(n)) + 1
    for i in range(2, n_sqrt):
        if n % i == 0:
            return False
    return True

class Node:

    def __init__(self, val, left_node=None, right_node=None):
        self.val = val
        self.left_node = left_node
        self.right_node = right_node

