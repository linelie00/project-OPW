from collections import Counter

word = [w.upper() for w in list(input())]
counter = Counter(word)
max_value = max(counter.values())
modes = [k for k, v in counter.items() if v == max_value]
if len(modes) > 1:
    print('?')
else:
    print(modes[0])