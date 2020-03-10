import sys
import math

sys.stdin = open('grades.txt', 'r')

for t in range(1, int(input())+1):
    N, K = list(map(int, input().split()))
    grades = []
    for i in range(N):
        x = list(map(int, input().split()))
        grades.append(round(x[0]*0.35+x[1]*0.45+x[2]*0.2,2))
    find = grades[K-1]
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    grades = sorted(grades, reverse=True)
    g_range = N//10
    for i in range(N):
        if grades[i] == find:
            print(grade[int(i/g_range)])
