
def main():
    max_val = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            n = i * j
            if is_palindrome(n) and n > max_val:
                max_val = n
    print max_val

def is_palindrome(n):
    n_str = str(n)
    whole = len(n_str)
    half = whole/2
    n_str_half = n_str[0:half]
    n_str_other_half = n_str[half:whole]
    return n_str_half[::-1] == n_str_other_half

if __name__ == '__main__':
    main()
