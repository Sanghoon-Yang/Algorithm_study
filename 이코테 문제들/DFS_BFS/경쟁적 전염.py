#N X N크기의 시험관
#특정위치에 바이러스가 존재 가능
#바이러스의 종류는 1~K번 까지 있음
#시험관에 존재하는 모든 바이러스는 1초마다 상하좌우 방향으로 증식
#매초 번호가 낮은 종류의 바이러스 부터 먼저 증식
#이미 감염됐으면 더이상 못들어감
#S 초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램
from collections import deque
n,k = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
s,x,y = map(int, input().split())

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

virus_pos = []

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus_pos.append([graph[i][j],0,i,j])

virus_pos = sorted(virus_pos)

def bfs(graph, virus_pos):
    que = deque()
    for a in virus_pos:
        que.append(a)

    while que:
        type, time, p, q = que.popleft()
        if time == s:
            break

        for i in range(4):
            np,nq = p+dx[i], q+dy[i]

            if 0<=np<n and 0<=nq<n and graph[np][nq] == 0:
                graph[np][nq] = type
                time += 1
                que.append([type, time, np, nq])

    return graph[x-1][y-1]


print(bfs(graph, virus_pos))
print(graph)