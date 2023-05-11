# 다익스트라 알고리즘
import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)

        # 기존의 거리가 더 짧으면 패스
        if distance[node] < dist:
            continue

        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

INF = int(1e9)
n, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dijkstra(start)
print(distance[1:])
