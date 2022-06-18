# p.262 전보

import heapq

n, m, c = map(int, input().split())
inf = int(1e9)
graph = [[] for _ in range(n + 1)]
distance = [inf] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append([y, z])


def dijkstra(start):
    distance[start] = 0
    q = list()
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)

for i in range(n + 1):
    if distance[i] >= inf:
        distance[i] = -1
cnt = 0
for d in distance:
    if d >= 1:
        cnt += 1

print(cnt, max(distance))
