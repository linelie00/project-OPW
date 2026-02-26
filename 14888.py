N = int(input())
A = list(map(int,input().split()))
ops_num = list(map(int,input().split()))

def div(x, y):
    if x < 0:
        return -(-x // y)
    return x // y

ops = [
    lambda x,y: x+y,
    lambda x,y: x-y,
    lambda x,y: x*y,
    div
]

max_v = -10**15
min_v = 10**15

def find(idx, v):
    global max_v, min_v

    if idx == N:
        max_v = max(max_v, v)
        min_v = min(min_v, v)
        return

    for i in range(4):
        if ops_num[i] > 0:
            ops_num[i] -= 1
            find(idx+1, ops[i](v, A[idx]))
            ops_num[i] += 1

find(1,A[0])
print(max_v)
print(min_v)