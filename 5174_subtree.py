for t in range(1, int(input()) + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    stack = [N]
    cnt = 1
    while len(stack) != 0:
        x = stack.pop()
        for i in range(0, len(arr), 2):
            if arr[i] == x:
                cnt += 1
                stack.append(arr[i + 1])
    print('#{} {}'.format(t, cnt))