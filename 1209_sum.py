case = 10
for test in range(10):
    T = int(input())
    matrix = [list(map(int, input().split())) for x in range(100)]
    row = []
    line = []
    cross = []
    sum_c = 0
    sum_r = 0
    sum_l = 0
    for i in range(100):
        for j in range(100):
            sum_r += matrix[i][j]
            sum_l += matrix[j][i]
            sum_c += matrix[j][j]
        row.append(sum_r)
        line.append(sum_l)
        cross.append(sum_c)
    max_r = max(row)
    max_l = max(line)
    max_c = max(cross)
    result = max(max_c, max_l, max_r)
    print('#{} {}'.format(T, result))