for t in range(1, int(input()) + 1):
    N = int(input())
    plate = [[0] * 10 for _ in range(10)]
    case = []
    count = 0
    for i in range(N):
        case.append(list(map(int, input().split())))
        for j in range(case[i][0], case[i][2] + 1):
            for k in range(case[i][1], case[i][3] + 1):
                plate[j][k] += case[i][4]
                if plate[j][k] == 3:
                    count += 1
    print('#{} {}'.format(t, count))
