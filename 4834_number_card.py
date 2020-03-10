T = int(input())
for i in range(1, T+1):
    c = [0] * 12
    count = 0
    case = int(input())
    test = list(map(int, input()))
    diction = {}
    for j in test:
        if j not in diction.keys():
            diction[j] = 1
        else:
            diction[j] += 1
    def f1(x):
        return diction[x]
    key_max = max(diction.keys(), key=f1)
    key_min = min(diction.keys(), key=f1)
    if key_max == key_min:
        print('#{} {} {}'.format(i, max(test), diction[key_max]))
    else:
        print('#{} {} {}'.format(i, key_max, diction[key_max]))        