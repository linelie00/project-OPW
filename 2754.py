score = list(input())
if score[0] == 'A': num = 4.0
elif score[0] == 'B': num = 3.0
elif score[0] == 'C': num = 2.0
elif score[0] == 'D': num = 1.0

if score[0] == 'F': print(0.0)
elif score[1] == '+': num += 0.3
elif score[1] == '-': num -= 0.3

if score[0] != 'F': print(num)
