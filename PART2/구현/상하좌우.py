# p.110 상하좌우

N = int(input())
my_map = list(input().split())
res_y, res_x = 1, 1

for i in range(len(my_map)):
    d = my_map[i]
    if d == 'R':
        if res_x + 1 <= N:
            res_x += 1
    elif d == 'L':
        if res_x - 1 > 0:
            res_x -= 1
    elif d == 'D':
        if res_y + 1 <= N:
            res_y += 1
    else:
        if res_y - 1 > 0:
            res_y -= 1
print(res_x, res_y)



