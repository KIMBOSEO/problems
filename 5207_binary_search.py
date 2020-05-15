for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for num in B:
        l = 0
        r = N - 1
        flag = 0
        while True:
            m = (l + r) // 2
            if num >= A[m]:
                if num == A[m]:
                    cnt += 1
                    break

                l = m + 1
                if flag == 1:
                    break
                flag = 1
            elif num < A[m]:
                r = m - 1
                if flag == -1:
                    break
                flag = -1

    print('#{} {}'.format(t, cnt))