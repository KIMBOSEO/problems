def back(idx, ans):
    global N, mini
    if idx == N and ans < mini:
        mini = ans
        return
    if ans > mini:
        return
    for i in range(N):
        if not col[i] and ans <= mini:
            col[i] = 1
            back(idx + 1, ans + case[idx][i])
            col[i] = 0


for t in range(1, int(input()) + 1):
    N = int(input())
    case = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    mini = 987654321
    col = [0] * N
    back(0, ans)
    print('#{} {}'.format(t, mini))
