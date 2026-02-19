import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break

    n = arr[0]
    heights = arr[1:]

    stack = []
    answer = 0

    for i in range(n):
        start = i

        while stack and stack[-1][0] > heights[i]:
            h, idx = stack.pop()
            answer = max(answer, h * (i - idx))
            start = idx
        stack.append((heights[i], start))
        print(stack)

    # 스택에 남은 것들 처리
    for h, idx in stack:
        answer = max(answer, h * (n - idx))

    print(answer)