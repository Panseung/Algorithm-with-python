# p.201 떡볶이 떡 만들기

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
rice_cakes = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = 1000000000
mid = (start + end) // 2
while start <= end:
    mid = (start + end) // 2
    length = 0
    for rice in rice_cakes:
        if rice > mid:
            length += rice - mid
    if length == M:
        break
    elif length < M:
        end = mid - 1
    else:
        start = mid + 1
print(mid)
