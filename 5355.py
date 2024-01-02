t = int(input())

for _ in range(t):
    num_list = list(map(str, input().split()))
    answer = 0
    for i in range(len(num_list)):
        if i == 0:
            answer += float(num_list[i])
        else:
            if num_list[i] == "#":
                answer -= 7
            elif num_list[i] == "%":
                answer += 5
            elif num_list[i] == "@":
                answer *= 3
                
    print("%0.2f" % answer)
