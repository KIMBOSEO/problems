for t in range(1, int(input()) + 1):
    N, M = map(str, input().split())
    ans = []
    for i in range(int(N)):
        if ord(M[i]) - ord('A') >= 0:
            k = int(ord(M[i]) - ord('A')) + 10
            a = format(k, 'b')
            if len(a) < 4:
                n = 4 - len(a)
                a = '0' * n + str(a)
            ans.append(a)
        else:
            a = format(int(M[i]), 'b')
            if len(a) < 4:
                n = 4 - len(a)
                a = '0' * n + str(a)
            ans.append(a)
    print('#{} {}'.format(t, ''.join(ans)))
