import sys

sys.stdin = open('swim.txt', 'r')


for TC in range(1, int(input()) + 1):
    N = int(input())
    calc = list(map(int, input().split()))
