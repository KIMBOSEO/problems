for t in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    graph = [[0] * (V + 1) for _ in range(V + 1)]

    for i in range(E):
        x, y, z = map(int, input().split())
        graph[x][y] = graph[y][x] = z

    INF = float('inf')
    key = [INF] * (V + 1)
    p = [0] * (V + 1)
    mst = [False] * (V + 1)

    key[0] = 0
    cnt = result = 0
    while cnt < V + 1:
        mini = INF
        u = -1
        for i in range(V + 1):
            if not mst[i] and key[i] < mini:
                mini = key[i]
                u = i
        mst[u] = True
        result += mini
        cnt += 1
        for w in range(V + 1):
            if not mst[w] and key[w] > graph[u][w] and graph[u][w] > 0:
                key[w] = graph[u][w]
                p[w] = u

    print('#{} {}'.format(t, result))