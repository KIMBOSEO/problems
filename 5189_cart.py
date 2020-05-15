import itertools

for t in range(1, int(input()) + 1):
    N = int(input())
    map_x = [list(map(int, input().split())) for _ in range(N)]
    arr = []
    for i in range(1, N):
        arr.append(i)
    n = len(arr)
    min_s = 9999
    case = list(itertools.permutations(arr, n))
    for i in range(len(case)):
        res = []
        res.append(0)
        for j in range(N - 1):
            res.append(case[i][j])
        res.append(0)
        sum = 0
        for j in range(len(res) - 1):
            sum += map_x[res[j]][res[j + 1]]

        if min_s > sum:
            min_s = sum
    print('#{} {}'.format(t, min_s))