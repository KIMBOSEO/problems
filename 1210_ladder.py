for a in range(10):
    t = int(input())
    ladd = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]
    for i in range(102):
        if ladd[99][i] == 2:
            break
    j = 99
    while True:
        if j == 0:
            break
        j -= 1
        if ladd[j][i-1] == 1:
            ladd[j][i] = 0
            i -= 1
            j += 1
        elif ladd[j][i+1] == 1:
            ladd[j][i] = 0
            i += 1
            j += 1
    print('#{} {}'.format(t, i-1))