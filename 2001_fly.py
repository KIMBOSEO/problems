T = int(input())
for t in range(1, T+1):
    kill = 0
    N, M = list(map(int, input().split()))
    area = [list(map(int, input().split())) for _ in range(N)]
    kill_list = []
    for i in range(N-M+1):
        for l in range(N - M + 1):
            for j in range(M):
                for k in range(M):
                    kill += area[i+j][k+l]
            kill_list.append(kill)
            kill = 0
    print('#{} {}'.format(t, max(kill_list)))