for t in range(1, int(input()) + 1):
    N = int(input())
    p = list(map(int, input().split()))
    ans = set([0])

    for x in p:
        num = set()
        for y in ans:
            num.add(x + y)
        ans = set(list(ans) + list(num))

    print('#{} {}'.format(t, len(set(ans))))