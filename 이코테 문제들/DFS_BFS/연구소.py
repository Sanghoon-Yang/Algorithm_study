
#인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출
#연구소는 크기가 NXM크기
#연구소는 빈칸, 벽으로 이루어져 있음
#바이러스는 상하좌우로 인접한 빈칸으로 모두 퍼져나갈 수 있슴
#새로 세울수 있는 벽의 개수는 3개

#itertools를 사용해서 벽을 세우는 모든 조건을 만들자.
#이후 dfs로 바이러슬ㄹ 퍼뜨리고
#안전영역의 크기를 구해보자

from itertools import combinations
from copy import deepcopy

N,M = map(int, input().split())
graph = []
temp = [[0]*M for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N):
    graph.append(list(map(int, input().split())))

empty_coodr = []
virus_coord = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            empty_coodr.append([i,j])
        elif graph[i][j] == 2:
            virus_coord.append([i,j])


def dfs_virus(graph, x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if graph[nx][ny] == 0:
                graph[nx][ny] == 2
                dfs_virus(nx, ny)


result = 0
cand = combinations(empty_coodr, 3)
#벽세우기
for c in cand:
    for i,j in c:
        graph[i][j] == 1

    for x,y in virus_coord:
        dfs_virus(x,y)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    result = max(cnt, result)

print(result)