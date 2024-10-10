import random

r = random.randint(1,10)
while(1):
    i = int(input('숫자를 맞춰보세요 : '))
    if i == r:
        print('정답입니다!')
        break
    else:
        print('틀렸습니다! 다시 시도해보세요...!')
        continue