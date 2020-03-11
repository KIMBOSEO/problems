for t in range(1, int(input()) + 1):
    case = list(map(str, input()))
    N = int(input())
    locat = list(map(int, input().split()))
    locat = sorted(locat, reverse=True)
    for i in (locat):
        case.insert(i, '-')
    print('#{} {}'.format(t, ''.join(case)))
