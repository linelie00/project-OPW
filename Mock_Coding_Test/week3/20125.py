import sys
input = sys.stdin.readline

N = int(input())

find_heart = False
find_arm = False
find_leg = False
left_arm = 0
right_arm = 0
waist = 0
left_leg = 0
right_leg = 0

for i in range(N):
    row = list(input().strip())
    if not find_heart:
        for j in range(N):
            if row[j] == '*':
                print(i+2,j+1)
                heart = [i+1,j]
                find_heart = True
    elif not find_arm:
        find_arm = True
        for j in range(N):
            if row[j] == '*':
                if j < heart[1]:
                    left_arm += 1
                elif j > heart[1]:
                    right_arm += 1
    elif not find_leg:
        for j in range(N):
            if j == heart[1] and row[j] == '*':
                waist += 1
            elif j == heart[1] and row[j] != '*':
                if row[j-1] == '*':
                    left_leg += 1
                if row[j+1] == '*':
                    right_leg += 1
print(left_arm,right_arm,waist,left_leg,right_leg)