for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    res = [0] * N
    for i in range(M):
        for j in range(N):
            if B[i] >= A[j]:
                res[j] += 1
                break
    print('#{} {}'.format(t, res.index(max(res))+1))