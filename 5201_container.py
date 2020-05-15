for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    w_lst = sorted(list(map(int, input().split())), reverse=True)
    t_lst = sorted(list(map(int, input().split())), reverse=True)
    i, j, sum = 0, 0, 0
    while True:
        if j == len(t_lst) or i == len(w_lst):
            break
        if w_lst[i] <= t_lst[j]:
            sum += w_lst[i]
            i += 1
            j += 1
        elif w_lst[i] > t_lst[j]:
            i += 1
    print('#{} {}'.format(t, sum))
