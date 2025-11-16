n = int(input())
for i in range(n):
    arr = []
    v = list(input())
    for j in v:
        if j == '(':
            arr.append('1')
        else:
            if not arr:
                print('NO')
                break
            arr.pop()
    else:
        if not arr:
            print('YES')
        else:
            print('NO')