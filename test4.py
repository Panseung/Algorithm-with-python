def solution(n, signs):
    answer = [[0] * n for _ in range(n)]
    for i in range(n):
        visited = [0] * n
        stack = []
        for j in range(n):
            if signs[i][j] == 0:
                continue
            stack.append(j)
            answer[i][j] = 1
        while stack:
            s = stack.pop()
            if visited[s] == 1:
                continue
            for k in range(n):
                if signs[s][k] == 0:
                    continue
                stack.append(k)
                visited[s] = 1
                answer[i][k] = 1
    print(answer)
    return answer


solution(3, [[0, 1, 0], [0, 0, 1], [1, 0, 0]])
