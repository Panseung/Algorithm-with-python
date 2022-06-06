# p.96 숫자 카드 게임

N, M = map(int, input().split())
result = list()
for i in range(N):
    result.append(min(list(map(int, input().split()))))
print(max(result))

