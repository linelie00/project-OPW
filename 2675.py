t = int(input())

for i in range(t):
    n, word = input().split()
    for j in word:
        print(j*int(n), end='') # end='' 옆으로 붙인다
    print()
