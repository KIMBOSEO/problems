T = int(input())
for t in range(1, T+1):
    X = True
    count_S, count_D, count_H, count_C = 13, 13, 13, 13
    s = list(map(str, input().split()))
    new_t = ''.join(s)
    types = 'SDHC'
    k = []
    for i in range(round(len(new_t)/3)):
        k.append(new_t[3*i]+new_t[3 * i + 1]+new_t[3 * i + 2])
    for m in range(len(k)):
        if 'S' in k[m]:
            count_S -= 1
        if 'D' in k[m]:
            count_D -= 1
        if 'H' in k[m]:
            count_H -= 1
        if 'C' in k[m]:
            count_C -= 1

# print(k[2])

    for j in range(len(k)):
        for l in range(len(k)):
            if j != l and k[j] == k[l]:
                X = False

    if X == True:
        print('#{} {} {} {} {}'.format(t, count_S, count_D, count_H, count_C))
    elif X == False:
        print('#{} ERROR'.format(t))

