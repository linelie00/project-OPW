arr = [input() for _ in range(3)]
anw = 0
for i in range(3):
    if arr[i] != 'Fizz' and arr[i] != 'Buzz' and arr[i] != 'FizzBuzz':
        anw = int(arr[i])+3-i
        if anw%3 == 0 and anw%5 == 0:
            print('FizzBuzz')
        elif anw%3 == 0:
            print('Fizz')
        elif anw%5 == 0:
            print('Buzz')
        else:
            print(anw)
        break