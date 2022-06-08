# p.220 개미 전사

import sys

N = int(input())
storage = list(map(int, sys.stdin.readline().rstrip().split()))

d = [0] * N
d[0] = storage[0]
d[1] = max(storage[0], storage[1])
for i in range(2, N):
    d[i] = max(d[i - 1], storage[i] + d[i - 2])

print(d[N - 1])