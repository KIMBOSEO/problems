for t in range(1, int(input())+1):
    case = list(map(str, input().split()))
    count, i = 0, 0
    B = len(case[1])
    #for i in range(len(case[0])):
    while i < len(case[0]):
        if case[0][i:i+B] == case[1]:
            count += 1
            i += B
        else:
            i += 1
    print('#{} {}'.format(t, len(case[0])-count*(B-1)))