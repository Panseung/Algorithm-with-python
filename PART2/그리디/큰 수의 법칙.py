# p.92 큰 수의 법칙

N, M, K = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
result = 0
turn = 0
cnt = 0
plus_num = lst[0]
while turn < M:
    turn += 1
    cnt += 1
    result += plus_num
    if cnt == K:
        plus_num = lst[1]
    elif cnt > K:
        cnt = 0
        plus_num = lst[0]

print(result)
