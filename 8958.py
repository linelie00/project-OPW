t = int(input())

for i in range(t):
    string = input()
    l = list(string)
    score = 0
    p = 0
    for j in l:
        if j == 'O':
           p += 1 
           score += p
        else:
            p = 0
    print(score)
