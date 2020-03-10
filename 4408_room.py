for t in range(1, int(input()) + 1):
    N = int(input())
    case = []
    count = 1
    res = [0] * 200
    for i in range(N):
        n_list = (list(map(int, input().split())))
        if n_list[0] > n_list[1]:
            n_list[0], n_list[1] = n_list[1], n_list[0]
        if n_list[0] % 2 == 0 and n_list[1] % 2 == 0:
            for i in range(n_list[0] // 2 - 1, n_list[1] // 2 - 1):
                res[i] += 1
        else:
            for i in range((n_list[0] + 1) // 2 - 1, (n_list[1] + 1) // 2):
                res[i] += 1
    print('#{} {}'.format(t, max(res)))
