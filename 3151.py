import sys
input = sys.stdin.readline

N = int(input())
student = list(map(int, input().split()))
student.sort()
cnt = 0

for i in range(N-2):

    # 가지치기1
    if student[i] > 0:
        break

    # 가지치기2
    if student[i] + student[i+1] + student[i+2] > 0:
        break
    if student[i] + student[N-1] + student[N-2] < 0:
        continue

    left = i+1
    right = N-1

    while left < right:
        s = student[i] + student[left] + student[right]
        if s == 0:
            # left와 right의 값이 같을 경우
            if student[left] == student[right]:
                n = right - left + 1
                cnt += n*(n-1)//2
                break
            else:
                l_cnt = 1
                r_cnt = 1
                while left + 1 <right and student[left] == student[left+1]:
                    left += 1
                    l_cnt += 1
                while right - 1 > left and student[right] == student[right-1]:
                    right -= 1
                    r_cnt += 1
                cnt += l_cnt*r_cnt
                left += 1
                right -= 1
        elif s < 0: #작을 경우 left움직이기
            left += 1
        else: #클 경우 right 움직이기
            right -= 1

print(cnt)