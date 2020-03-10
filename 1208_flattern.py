tc = 10
for i in range(0, tc):
    count = 0
    Max = int(input())
    x = list(map(int, input().split()))
    x.sort()
    for j in range(0, 1000):
        max = x[-1]
        min = x[0]
        k = max - min
        x[-1] -= 1
        x[0] += 1
        count += 1
        x.sort()
        if count == Max + 1:
            print('#{} {}'.format(i + 1, k))


