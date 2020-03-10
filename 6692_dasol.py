import sys

sys.stdin = open('grades.txt', 'r')


for t in range(1, int(input()) + 1):
    N = int(input())
    res = []
    for i in range(N):
        case = list(map(float, input().split()))
        res.append(case[0] * case[1])
    ans = sum(res)
    print('#{} {:,.6f}'.format(t, ans))
