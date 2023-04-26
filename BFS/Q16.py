from itertools import combinations
from copy import deepcopy
n,m = map(int, input().split())

graph = []
temp = [[0] * m  for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 0
empty_cor = []
virus_cor = []


def virus(temp,x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < n  and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(temp,nx,ny)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty_cor.append((i,j))
        if graph[i][j] == 2:
            virus_cor.append((i,j))


candidate = combinations(empty_cor,3)

for cand in candidate:
    temp = deepcopy(graph)

    for i,j in cand:
        temp[i][j] = 1

    for i,j in virus_cor:
        virus(temp, i,j)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1

    result = max(cnt, result)

print(result)
