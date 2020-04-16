for t in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    case = list(map(int, input().split()))
    n = 0
    for i in range(1, K + 1):
        n += M
        if n < N:
            case.insert(n, case[n - 1] + case[n])
        else:
            if n % N:
                n = n % N
                case.insert(n, case[n - 1] + case[n])
            else:
                case.insert(n, case[- 1] + case[0])
        N += 1
    print('#{} '.format(t), end='')
    print(' '.join(map(str, case[-1:-11:-1])))
