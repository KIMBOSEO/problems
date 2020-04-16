for t in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    case = list(map(int, input().split()))
    for i in range(M):
        a, b = map(int, input().split())
        case.insert(a, b)
    print('#{} {}'.format(t, case[L]))