t = int(input())
for _ in range(t):
    n = int(input())
    s = []*2
    s.append(list(map(int, input().split())))
    s.append(list(map(int, input().split())))

    if n == 1:
        print(max(s[0][-1],s[1][-1]))
        continue

    s[0][1] += s[1][0]
    s[1][1] += s[0][0]

    if n == 2:
        print(max(s[0][-1],s[1][-1]))
        continue
    
    for i in range(2, n):
        s[0][i] += max(s[1][i-1],s[1][i-2])
        s[1][i] += max(s[0][i-1],s[0][i-2])
    print(max(s[0][-1],s[1][-1]))