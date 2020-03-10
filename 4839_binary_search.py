T = int(input())
for t in range(1, T+1):
    P, A, B = list(map(int,input().split()))
    l = 1
    k = P
    count_A = 0
    count_B = 0
    for i in range(0, 1000):
        c = int((l + k)/2)
        count_A += 1
        if c < A:
            l = c
        if c > A:
            k = c
        if c == A:
            break
    l = 1
    k = P
    for j in range(0, 1000):
        c = int((l+k)/2)
        count_B += 1
        if c < B:
            l = c
        if c > B:
            k = c
        if c == B:
            break
    if count_A < count_B:
        print('#{} A'.format(t))
    if count_A > count_B:
        print('#{} B'.format(t))
    if count_A == count_B:
        print('#{} 0'.format(t))
