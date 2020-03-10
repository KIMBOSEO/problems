T = int(input())
for t in range(1, T+1):
    name = str(input())
    x = len(name) * 4 + 1
    y = len(name) * 4 - 1
    z = ['.']*x
    for i in range(int(x/2)):
        z[2*i+1] = '#'
    a = z
    a = ''.join(a)
    z = ['.'] * x
    for j in range(len(name)):
        z[4*(j+1)-2] = '#'
    b = z
    b = ''.join(b)
    z = ['.'] * x
    for k in range(int(x/4)):
        z[4*k + 2] = name[k]
    for k in range(int(x/4)+1):
        z[4*k] = '#'
    c = z
    c = ''.join(c)
    print(b)
    print(a)
    print(c)
    print(a)
    print(b)