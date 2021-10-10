
   
import sys
from heapq import heappop, heappush

n, m = map(int, sys.stdin.readline().split())
visit, graph = dict(), dict()
node = list(sys.stdin.readline().split())

for item in node:
    visit[item] = 0
    graph[item] = []

for i in range(m):
    a, b, wei = sys.stdin.readline().split()
    graph[a].append((int(wei), b))
    graph[b].append((int(wei), a))

visit[node[0]] = 1
edge, ans = [], 0
for wei, b in graph[node[0]]:
    heappush(edge, (wei, b))

while edge:
    wei, now_node = heappop(edge)

    if visit[now_node] == 1:
        continue

    visit[now_node] = 1
    ans += wei
    for wei, next_node in graph[now_node]:
        if visit[next_node] == 0:
            heappush(edge, (wei, next_node))


print(ans)
