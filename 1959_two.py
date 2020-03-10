T = int(input())
for t in range(1, T+1):
    sum_list = []
    sum = 0
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if len(A) <= len(B):
        for i in range(len(B) - len(A) + 1):
            for j in range(len(A)):
                sum += A[j]*B[j+i]
            sum_list.append(sum)
            sum = 0
    if len(A) > len(B):
        A, B = B, A
        for i in range(len(B) - len(A) + 1):
            for j in range(len(A)):
                sum += A[j]*B[j+i]
            sum_list.append(sum)
            sum = 0
    sum_list = sorted(sum_list)
    print('#{} {}'.format(t, sum_list[-1]))