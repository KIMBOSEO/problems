for t in range(1, int(input()) + 1):
    N = int(input())
    stack = []
    for i in range(N):
        stack.append(list(map(int, input().split())))
    for i in range(N):
        for j in range(i, N):
            if stack[i][1] > stack[j][1]:
                stack[i], stack[j] = stack[j], stack[i]

    result = []
    visited = [0] * N
    result.append(stack[0])
    visited[0] = 1
    while True:
        for i in range(N):
            if result[-1][-1] > stack[i][0]:
                visited[i] = 1

        if not 0 in visited:
            break

        index = 0
        value = 987654321
        for i in range(N):
            if visited[i] == 0 and result[-1][-1] <= stack[i][0] and stack[i][1] < value:
                index = i
                value = stack[i][0]

        result.append(stack[index])

    print('#%d %d' % (t, len(result)))