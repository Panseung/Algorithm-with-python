# p.118 게임 개발
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def move(r):
    global y, x, d, Next
    if r == 0:
        r = 3
    else:
        r -= 1

    result = False

    for i in range(4):
        direc = (r + i) % 4
        ry = y + dy[direc]
        rx = x + dx[direc]
        if 0 <= ry < N and 0 <= rx < M and not brd[ry][rx] and not visited[ry][rx]:
            visited[ry][rx] = 1
            y = ry
            x = rx
            d = direc
            result = True
            break
    if result:
        return
    else:
        direc = (r + 2) % 4
        y += dy[direc]
        x += dx[direc]
        if brd[y][x] == 0:
            return
        else:
            Next = False
            return


N, M = map(int, input().split())
y, x, d = map(int, input().split())

brd = list()
for _ in range(N):
    brd.append(list(map(int, input().split())))
visited = [[0] * M for _ in range(N)]
visited[y][x] = 1

Next = True
while Next:
    move(d)

cnt = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 1:
            cnt += 1

print(cnt)
