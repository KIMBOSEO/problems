T = int(input())
for t in range(1, T+1):
    print('#{}'.format(t))
    N = int(input())
    case = [list(map(int, input().split())) for _ in range(N)]
    rot_1 = []
    rot_2 = []
    rot_3 = []
    result = []
    for i in range(N):
        for j in range(N):
            rot_1.append(case[-j-1][i])
            rot_2.append(case[-i-1][-j-1])
            rot_3.append(case[j][-i-1])
        result.append(rot_1)
        result.append(rot_2)
        result.append(rot_3)
    for i in range(N):
        for j in range(3):
            print("".join(map(str,(result[j][N*i:(i+1)*N]))), end=' ')
        print()

