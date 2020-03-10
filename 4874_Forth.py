T = int(input())
for t in range(1, T+1):
    print('#{} '.format(t), end='')
    code = list(map(str, input().split()))
    con = '+-*/'
    stack = []
    for i in code:
        if i in con:
            if len(stack) < 2:
                # print('error')
                break
            if i == '+':
                act = int(stack.pop(-2)) + int(stack.pop(-1))
                stack.append(act)
            elif i == '-':
                act = int(stack.pop(-2)) - int(stack.pop(-1))
                stack.append(act)
            elif i == '*':
                act = int(stack.pop(-2)) * int(stack.pop(-1))
                stack.append(act)
            elif i == '/':
                act = int(stack.pop(-2)) // int(stack.pop(-1))
                stack.append(act)

        else:
            stack.append(i)
    if len(stack) == 2 and stack[-1] == '.':
        print(stack.pop(-2))
    else:
        print('error')
