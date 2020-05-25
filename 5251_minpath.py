for t in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    graph = {i: [] for i in range(V + 1)}
    for i in range(E):
        s, e, c = map(int, input().split())
        graph[s].append([e, c])

    INF = float('inf')
    dist = [INF] * (V + 1)
    selected = [False] * (V + 1)
    dist[0] = 0
    cnt = 0
    while cnt < V + 1:
        min = INF
        u = -1
        for i in range(V + 1):
            if not selected[i] and dist[i] < min:
                min = dist[i]
                u = i

        cnt += 1
        selected[u] = True
        for w, cost in graph[u]:
            if dist[w] > dist[u] + cost:
                dist[w] = dist[u] + cost

    print('#{} {}'.format(t, dist[V]))