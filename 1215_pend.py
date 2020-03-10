for t in range(1, 11):
    print('#{}'.format(t), end=' ')
    N = int(input())
    count = 0
    case = [list(map(str, input())) for _ in range(8)]
    result =0
    result_l = 0
    count_l = 0
    res = []
    res_l = []
    # 가로 찾기
    for i in range(8):
        for j in range(9 - N):
            if case[i][j] == case[i][j+N-1]:
                for k in range(1, int(N/2)):
                    if case[i][j+k] == case[i][j+N-1-k]:
                        count += 1
                        res.append(case[i][j+k])
                if count == int(N/2)-1:
                    result += 1
                    count = 0
                count = 0
    # 세로줄
    for i in range(8):
        for j in range(9 - N):
            if case[j][i] == case[j+N-1][i]:
                for k in range(1, int(N/2)):
                    if case[j+k][i] == case[j+N-1-k][i]:
                        count_l += 1
                        res_l.append(case[i][j+k])
                if count_l == int(N/2)-1:
                    result_l += 1
                    count_l = 0
                count_l = 0
    print(result_l+result)