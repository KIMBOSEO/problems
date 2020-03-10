for i in range(0,10):
    count = 0
    T = int(input())
    x= input().split()
    x= list(map(int, x))
    for j in range(2, T-2):
        l_max = max(x[j-1], x[j-2])
        r_max = max(x[j+1], x[j+2])
        real_max = max(l_max, r_max)
        if x[j] > real_max:
        	count += x[j] - int(real_max)
    print('#{} {}'.format(i+1, count))