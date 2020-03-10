T = int(input())
for t in range(1, T+1):
    letter = [list(map(str, ''.join(input().split()))) for _ in range(0, 5)]
    blank = [['.'] * len(letter[0]) for _ in range(5)]
    max = 0
    new_list = []
    for i in range(5):
        if len(letter[i]) > max:
            max = len(letter[i])
    for i in range(max):
        for j in range(5):
            if len(letter[j]) < max:
                letter[j] += '!'
            new_list.append(letter[j][i])
    print('#{} {}'.format(t, ''.join(new_list).replace('!', '')))