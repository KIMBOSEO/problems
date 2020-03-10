T = int(input())
for i in range(0, T):
    number = int(input())
    numbers = input().split()
    new_m = list(map(int, numbers))
    new_m.sort()
    sub = new_m[-1] - new_m[0]
    print('#{} {}'.format(i+1, sub))
