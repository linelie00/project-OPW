import sys
input = sys.stdin.readline

N = int(input())
s = [list(map(int,input().split())) for _ in range(N)]
ans = 10*15

def find(idx,start,link,st_pw,li_pw):
    global ans
    
    #다 넣었을 때
    if idx == N:
        ans = min(ans,abs(st_pw-li_pw))
        return
    #스타트팀에 넣을 때
    if len(start) < N//2:
        temp = 0
        if start:
            temp = st_pw
            for x in start:
                temp += s[x][idx] + s[idx][x]
        find(idx+1,start+[idx],link,temp,li_pw)
    #링크팀에 넣을 때
    if len(link) < N//2:
        temp = 0
        if link:
            temp = li_pw
            for x in link:
                temp += s[x][idx] + s[idx][x]
        find(idx+1,start,link+[idx],st_pw,temp)

find(0,[],[],0,0)
print(ans)