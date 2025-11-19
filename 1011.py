def find_range_index(k):
    total = 0
    i = 0 
    while total < k:
        i += 1
        length = (i + 1) // 2
        total += length
    return i

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(find_range_index(y-x))
    
# 1 1 / 1
# 2 2 / 1 1
# 3 3 / 1 1 1
# 4 3 / 1 2 1
# 5 4 / 1 2 1 1
# 6 4 / 1 2 2 1
# 7 5 / 1 2 2 1 1
# 8 5 / 1 2 2 2 1
# 9 5 / 1 2 3 2 1
# 10 6 / 1 2 2 2 2 1
# 11 6 / 1 2 3 2 2 1
# 12 6 / 1 2 3 3 2 1
# 13 7 / 1 2 2 3 2 2 1
# 14 7 / 1 2 3 3 2 2 1
# 15 7 / 1 2 3 3 3 2 1
# 16 7 / 1 2 3 4 3 2 1
# 17 8 /
# 18 8 /
# 19 8 /
# 20 8 / 1 2 3 4 4 3 2 1

#25 / 1 2 3 4 5 4 3 2 1
#30 / 