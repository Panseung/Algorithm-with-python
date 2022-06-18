# p.237

import sys

inf = int(1e9)

n, m = map(int, sys.stdin.readline().rstrip().split())
start = int(input())

graph = [[] for _ in range(n + 1)]

visited = [False] * (n + 1)

distance = [inf] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])


def get_smallest_node():
    index = 0
    min_value = inf
    for k in range(1, n + 1):
        if not visited[k] and distance[k] < min_value:
            min_value = distance[k]
            index = k
    return index


def dijkstra(start):
    visited[start] = True
    distance[start] = 0

    for i in graph[start]:
        distance[i[0]] = i[1]

    for i in range(n - 1):
        idx = get_smallest_node()
        visited[idx] = True
        for j in graph[idx]:
            cost = distance[idx] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == inf:
        print(-1)
    else:
        print(distance[i])
