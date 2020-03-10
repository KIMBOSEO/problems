T = int(input())
for t in range(1, T+1):
    print('#{}'.format(t))
    num = str(input().split())
    case = list(map(str, input().split()))
    result = []
    rng = len(case)
    for i in range(rng):
        if case[i] == 'ZRO':
            result.append(case[i])
    for i in range(rng):
        if case[i] == 'ONE':
            result.append(case[i])
    for i in range(rng):
        if case[i] == 'TWO':
            result.append(case[i])
    for i in range(rng):
        if case[i] == 'THR':
            result.append(case[i])
    for i in range(rng):
        if case[i] == 'FOR':
            result.append(case[i])
    for i in range(rng):
        if case[i] == 'FIV':
            result.append(case[i])
    for i in range(rng):
        if case[i] == 'SIX':
            result.append(case[i])
    for i in range(rng):
        if case[i] == 'SVN':
            result.append(case[i])
    for i in range(rng):
        if case[i] == 'EGT':
            result.append(case[i])
    for i in range(rng):
        if case[i] == 'NIN':
            result.append(case[i])
    result = ' '.join(result)
    print(result)

