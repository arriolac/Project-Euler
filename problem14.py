def collatz_sequence(n):
    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
        seq.append(n)
    return seq

def main():
    longest_chain_length = 0
    longest_seed = 0
    for i in range(1, 1000001):
        seq = collatz_sequence(i)
        len_seq = len(seq)
        if len_seq > longest_chain_length:
            longest_chain_length = len_seq
            longest_seed = i
    print "Longest sequence length: {}".format(longest_chain_length)
    print "Starting number: {}".format(longest_seed)

if __name__ == '__main__':
    main()
