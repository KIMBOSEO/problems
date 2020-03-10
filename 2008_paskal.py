T = int(input())
for t in range(1, T+1):
    print('#{}'.format(t))
    print('1')
    N = int(input())
    k = [0] * N
    k[-1] = 1
    for i in range(2, N+1):
        result =[0] * i
        result[0] = 1
        result[-1] = 1
        k[i-2] = result
        if i > 2:
            result[1] = i - 1
            for j in range(2, i-1):
                result[j] = k[i-3][j-1]+k[i-3][j]
    for i in range(1, t):
        print(' '.join(map(str, k[i-1])))