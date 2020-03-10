import sys

sys.stdin = open('grades.txt', 'r')

for t in range(1, int(input())+1):
    case = list(map(int, input()))
    res = [0] * len(case)
    count = 0
    for i in range(len(case)):
        if res[i] != case[i] and case[i] == 1:
            for j in range(i, len(res)):
                res[j] = 1
            count += 1
        elif res[i] != case[i] and case[i] == 0:
            for j in range(i, len(res)):
                res[j] = 0
            count += 1

    print(count)