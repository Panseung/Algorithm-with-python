# p.115 왕실의 나이트

N = input()
x = ord(N[0]) - 96
y = int(N[1])

dy = [-2, -2, -1, 1, 2, 2, -1, 1]
dx = [-1, 1, 2, 2, -1, 1, -2, -2]

cnt = 0
for i in range(8):
    ry = y + dy[i]
    rx = x + dx[i]
    if 1 <= ry <= 8 and 1 <= rx <= 8:
        cnt += 1

print(cnt)
