#1~N번까지의 도시와 M개의 단방향 도로가 존재
#모든 도로의 거리는 1
#특정 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서 최단거리가 정확히 K인 도시의 번호를 출력

# 모든 도로의 거리는 1이라는 조건때문에 bfs 로 풀어야할듯
from collections import deque


N,M,K,X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)

distance = [-1]*(N+1)
distance[X] = 0

que = deque()
que.append([X])

while que:
    x = que.popleft()
    for city in graph[x]:
        if distance[city] == -1: #방문을 하지 않았다면,
            distance[city] = distance[x] + 1
            que.append([city])

check = False
for i in range(N+1):
    if distance[i] == K:
        print(i)
        check = True

if check == False:
    print(-1)
