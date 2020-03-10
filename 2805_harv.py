T = int(input())
for t in range(1, T+1):
    sum = 0
    size = []
    N = int(input())
    for i in range(N):
        size.append(input())
    for i in range(N):
        if i > int(N/2):
            l = 2*int(N/2)-i
            for j in range(int(N / 2) - l, int(N / 2) + l + 1):
                sum += int(size[i][j])
        else:
            for j in range(int(N/2)-i, int(N/2)+i+1):
                sum += int(size[i][j])
    print('#{} {}'.format(t, sum))