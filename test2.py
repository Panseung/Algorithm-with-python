def solution(dirs):
    answer = 0
    visited = [[[0] * 2 for _ in range(11)] for _ in range(11)]
    pos_y, pos_x = 5, 5
    for d in dirs:
        if d == 'U' and pos_y > 0:
            pos_y -= 1
            if visited[pos_y][pos_x][0] == 0:
                visited[pos_y][pos_x][0] = 1
                answer += 1
        if d == 'D' and pos_y < 10:
            pos_y += 1
            if visited[pos_y - 1][pos_x][0] == 0:
                visited[pos_y - 1][pos_x][0] = 1
                answer += 1
        if d == 'L' and pos_x > 0:
            pos_x -= 1
            if visited[pos_y][pos_x][1] == 0:
                visited[pos_y][pos_x][1] = 1
                answer += 1
        elif d == 'R' and pos_x < 10:
            pos_x += 1
            if visited[pos_y][pos_x - 1][1] == 0:
                visited[pos_y][pos_x - 1][1] = 1
                answer += 1
    return answer

solution('ULURRDLLU')