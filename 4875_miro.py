def find(a, x, y):
    global ans
    visited[y][x] = 1
    if a[y][x] == 3:
        ans = 1
        return ans
    else:
        for i in range(4):
            wx = x + dir_x[i]
            wy = y + dir_y[i]
            if a[wy][wx] == 0 and visited[wy][wx] == 0:
                find(a, wx, wy)
            if a[wy][wx] == 3 and visited[wy][wx] == 0:
                find(a, wx, wy)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    ans = 0
    plus = [1]*(N+2)
    maze =[plus] + [[1] + list(map(int, input())) + [1] for _ in range(N)] + [plus]
    dir_x = [1, 0, -1, 0]   #오위왼아
    dir_y = [0, -1, 0, 1]
    visited = [[0] *(N+2) for _ in range(N+2)]
    for i in range(N+2):
        for j in range(N+2):
            if maze[i][j] == 2:
                x, y = j, i
                break
    find(maze, x, y)
    print('#{} {}'.format(t, ans))