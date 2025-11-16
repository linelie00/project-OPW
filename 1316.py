from collections import Counter
n = int(input())
count = 0

for i in range(n):
    str = input()
    str_count = Counter(list(str))
    for j in list(str):
        if str.find(j * str_count[j]) == -1:
            break
    else:
        count += 1

print(count)