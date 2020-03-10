T = int(input())
for test in range(1, T+1):
    num = int(input())
    num_list = list(map(int, input().split()))
    half = int(num / 2)
    result = [0]*10
    num_list = sorted(num_list)
    for i in range(half):
        result[2*i] = num_list[-i-1]
        result[2*i+1] = num_list[i]
        if result[-1] > 0:
            break
    result = list(map(str, result))
    result = ' '.join(result)
    print('#{} {}'.format(test, result))