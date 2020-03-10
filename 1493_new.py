T = int(input())
for t in range(1, T+1):
    sum_p = 0
    sum_q = 0
    p,q = list(map(int, input().split()))
    for i in range(1, 150):
        sum_p += i
        if p <= sum_p:
            num_p = sum_p - p
            px = i - num_p
            py = num_p + 1
            break
    for j in range(1, 150):
        sum_q += j
        if q <= sum_q:
            num_q = sum_q - q
            qx = j - num_q
            qy = 1 + num_q
            break
    res_x = px+qx
    res_y = py+qy
    ans = 0
    for k in range(1, res_x+1):
        ans += k
    for m in range(k, k+res_y-1):
        ans += m
    print('#{} {}'.format(t,ans))