from collections import deque

n,k = map(int, input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j],0,i,j))





dx = [-1,1,0,0]
dy = [0,0,-1,1]


data.sort()
q = deque(data)


ts,tx,ty = map(int,input().split())

while q:
    virus, time, x, y = q.popleft()
    if time == ts:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dx[i]

        if 0 <= nx and  0 <= ny and nx < n and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, time + 1, nx,ny))


print(graph)
print(graph[tx-1][ty-1])
