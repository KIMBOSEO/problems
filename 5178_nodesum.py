for t in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    case = [0]*(N+2)
    for i in range(M):
        a, b = map(int, input().split())
        case[a] = b
    for j in range(N+1, 1, -1):
        if (j // 2) == (j-1)// 2:
            case[(j // 2)] = case[j] + case[j-1]
    print('#{} {}'.format(t, case[L]))