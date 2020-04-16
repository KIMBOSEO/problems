T = int(input())

for tc in range(T):
    # input
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split())) # 처음 거는 인풋 받아서 만들고
    for _ in range(M-1): # 그 다음부터는 이전 거랑 비교
        temp_numbers = list(map(int, input().split()))
        for idx in range(len(numbers)):
            if numbers[idx] > temp_numbers[0]:
                numbers[idx:idx] = temp_numbers
                break
        else: # break에 걸리지 않은 경우
            numbers += temp_numbers
    print("#%d %s" %(tc+1, ' '.join(list(map(str,numbers[::-1][:10])))))