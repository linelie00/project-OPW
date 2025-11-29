n = int(input())
stack = []
cnt = 0

for _ in range(n):
    h = int(input())
    same = 1

    # 작은 키는 pop됨
    while stack and stack[-1][0] < h:
        cnt += stack[-1][1]
        stack.pop()

    # 같은 키가 나오면 묶어서 처리
    if stack and stack[-1][0] == h:
        cnt += stack[-1][1]     # 같은 키 모두 볼 수 있음
        same = stack[-1][1] + 1
        stack.pop()

        # 앞에 더 큰 키가 남아 있다면 1명은 더 볼 수 있음
        if stack:
            cnt += 1
    else:
        # 앞에 더 큰 키가 있는 경우 1명 더 볼 수 있음
        if stack:
            cnt += 1

    stack.append((h, same))

print(cnt)


# 3 2 1 3
# 3 2 1 1 3 / 4
# 4 1 2 2 5
# 3 2 2 1 1 3
# 3 2 2 2 2 2 3

# 5 4 3 2 1 5
# 5 4 3 1 1 5
# 3 -> 1
# 4 -> 

# 3 2 2 1 3 / 4+3+1
# 3 

# 2 1 1 2 /3+3

# 3 2 2 1 1 3 / 5+4+2
# 3 3 2 2 1 1 / 5+2

# 3 3 3 1 / 3+1
# 4 4 4 3 3 1 / 5+2
# 4 5 5 1 1 /4+1