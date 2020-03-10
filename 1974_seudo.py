T = int(input())
for t in range(1, T+1):
    print('#{}'.format(t), end=' ')
    count = 0
    result = []
    res = []
    case = [list(map(int, input().split())) for _ in range(9)]
    for i in range(9):
        for j in range(8):
            if case[i][j+1] == case[i][0]:
                count += 1
            for k in range(1, 9-j):
                if case[i][j] == case[i][j+k]:
                    count += 1
                elif case[j][i] == case[j+k][i]:
                    count += 1
    for a in range(3):
        for b in range(3):
            for i in range(3):
                for j in range(3):
                    result.append(case[i+3*a][j+3*b])
            res.append(result)
            result = []
    for k in range(9):
        for l in range(1, 9):
            if res[k][0] == res[k][l]:
                count += 1


    if count == 0:
        print('1')
    else:
        print('0')



