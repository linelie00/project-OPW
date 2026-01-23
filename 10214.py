t = int(input())
for _ in range(t):
    cnt = 0
    for i in range(9):
        y,k = map(int, input().split())
        cnt += y-k
    print('Yonsei' if cnt > 0 else ('Korea' if cnt < 0 else 'Draw'))