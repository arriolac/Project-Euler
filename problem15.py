import math

def paths(n):

    matrix = [[0 for i in range(n+1)] for j in range(n+1)]

    # Borders are all 1:
    for i in range(n+1): matrix[n][i] = 1
    for i in range(n+1): matrix[i][n] = 1

    for i in range(1, n+1):
        for j in range(1, n+1):
            matrix[n-i][n-j] = matrix[n-i][n-j+1] + matrix[n-i+1][n-j]

    print_matrix(matrix)

    return matrix[0][0]

def print_matrix(mat):
    for row in mat:
        print row

def main(n):
    return paths(n)

if __name__ == '__main__':
    print main(20)
