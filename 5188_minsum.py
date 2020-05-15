def find(r, c, s):
    global min_x
    if r == N - 1 and c == N - 1 and min_x > s:
        min_x = s
        stack.append(s)
    else:
        if r < N - 1:
            find(r + 1, c, s + map_x[r + 1][c])
        if c < N - 1:
            find(r, c + 1, s + map_x[r][c + 1])


for t in range(1, int(input()) + 1):
    N = int(input())
    map_x = [list(map(int, input().split())) for _ in range(N)]
    min_x = 99999
    stack = []
    find(0, 0, map_x[0][0])
    print('#{} {}'.format(t, min(stack)))