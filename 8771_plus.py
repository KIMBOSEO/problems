import sys

sys.stdin = open('grades.txt', 'r')


def factorial(n):
    if n == 0:
        return 1
    else:
        for i in range(n):
            ans = i + factorial(i-1)
        print(ans)
    return ans


for t in range(1, int(input())+1):
    print('tt')
    N, A, B = list(map(int, input().split()))
    ans = 0
    if B-A+1 != N:
        print('0')
    else:
        num = B-A+1
        for i in range(num):
            for j in range(num-i):
                ans += j
    print(ans)

