# p.152 미로 탈출

from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, input().split())
maze = list()
for _ in range(N):
    maze.append(input())
visited = [[0] * M for _ in range(N)]

queue = deque()
queue.append([0, 0, 1])
find = False
while queue:
    y, x, d = queue.popleft()
    for i in range(4):
        ry = y + dy[i]
        rx = x + dx[i]
        if 0 <= ry < N and 0 <= rx < M and not visited[ry][rx] and maze[ry][rx] == '1':
            visited[ry][rx] = 1
            queue.append([ry, rx, d + 1])
            if ry == N - 1 and rx == M - 1:
                find = True
                print(d + 1)
                break
    if find:
        break


