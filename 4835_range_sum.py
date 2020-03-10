T = int(input())
for test_case in range(1, T + 1):
    a = 0
    b = []
    N = input().split()
    x = input().split()
    x = list(map(int, x))
    num = int(N[0]) - int(N[1])
    number = int(N[1])
    for i in range(0, num+1):
        for j in range(0, number):
            a += x[i+j]
        b.append(a)
        a = 0
    maximum =int(max(b))
    minimum = int(min(b))
    result = maximum - minimum
    print('#{} {}'.format(test_case, result))