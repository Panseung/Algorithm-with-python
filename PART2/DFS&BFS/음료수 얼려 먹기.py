# p.149 음료수 얼려 먹기

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def cream(y, x):
    for d in range(4):
        ry = y + dy[d]
        rx = x + dx[d]
        if 0 <= ry < N and 0 <= rx < M and not visited[ry][rx] and ice[ry][rx] == '0':
            visited[ry][rx] = 1
            cream(ry, rx)


N, M = map(int, input().split())
ice = list()
for _ in range(N):
    ice.append(input())

visited = [[0] * M for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if ice[i][j] == '0' and visited[i][j] == 0:
            cnt += 1
            cream(i, j)

print(cnt)