for t in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    case = list(map(str, input().split()))
    flag = -1
    for i in range(M):
        nums = list(map(str, input().split()))
        if nums[0] == 'I':
            case.insert(int(nums[1]), int(nums[2]))
        if nums[0] == 'D':
            del case[int(nums[1])]
        if nums[0] == 'C':
            case[int(nums[1])] = int(nums[2])

    print('#{}'.format(t), end=' ')
    if len(case) > L:
        print(case[L])
    else:
        print('-1')