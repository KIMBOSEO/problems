for t in range(1, int(input())+1):
    N = float(input())
    n= 0
    ans = []
    while n <13:
        if N == 0:
            break
        n += 1
        if N >= 2 ** (-n):
            N -= 2 ** (-n)
            ans.append(1)
        else:
            ans.append(0)
        #print(ans, n, N)
    if n == 13:
        print('#{} overflow'.format(t))
    else:
        print('#{} {}'.format(t, ''.join(map(str, ans))))