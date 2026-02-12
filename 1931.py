N = int(input())
meetings = [list(map(int,input().split())) for _ in range(N)]
meetings.sort(key=lambda x:(x[1], x[0]))
cnt = 0
end_time = 0

for (start, end) in meetings:
    if start >= end_time:
        end_time = end
        cnt += 1
print(cnt)