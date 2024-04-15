n = int(input())
if(n%10!=0):
    print(-1)
    exit()
print(n//300, end=' ')
n%=300
print(n//60, end=' ')
n%=60
print(n//10)
