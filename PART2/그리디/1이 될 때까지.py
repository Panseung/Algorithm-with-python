# p.99 1이 될 때까지

N, K = map(int, input().split())
cnt = 0

while N != 1:
    cnt += 1
    if N % K == 0:
        N /= K
    else:
        N -= 1

print(cnt)
