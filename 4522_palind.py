for t in range(1, int(input())+1):
    case = str(input())
    if len(case) ==1:
        ans =0
    for i in range(len(case)//2):
        if case[i] == case[-i-1]:
            ans =0
        else:
            if '?' == case[i] or case[-i-1] == '?':
                ans =0
            else:
                ans =1
                break
    if ans == 0:
        print('#{} Exist'.format(t))
    else:
        print('#{} Not exist'.format(t))