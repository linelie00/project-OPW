import sys
input = sys.stdin.readline

MOD = 1000000007

def mul(a, b):
    return [
        [(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % MOD,
         (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % MOD],

        [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % MOD,
         (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % MOD]
    ]

def power(matrix, n):
    if n == 1:
        return matrix

    half = power(matrix, n//2)

    if n % 2 == 0:
        return mul(half, half)
    else:
        return mul(mul(half, half), matrix)


n = int(input())

if n == 0:
    print(0)
else:
    base = [[1,1],[1,0]]
    result = power(base, n)
    print(result[0][1])