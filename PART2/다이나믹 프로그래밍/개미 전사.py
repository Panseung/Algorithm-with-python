# p.220 개미 전사

import sys


def dp(x, cnt):
    d[x] = max(d[x], cnt)
    if x + 2 < N:
        dp(x + 2, cnt + storage[x + 2])
    if x + 3 < N:
        dp(x + 3, cnt + storage[x + 3])


N = int(input())
storage = list(map(int, sys.stdin.readline().rstrip().split()))

d = [0] * N
dp(0, 1)
dp(1, 3)
print(max(d[N - 2], d[N - 1]))
