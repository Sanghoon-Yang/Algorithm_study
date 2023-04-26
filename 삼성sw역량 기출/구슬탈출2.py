from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

mapp = []

visited = []
q = deque()
rx, ry, bx, by = 0, 0, 0, 0

for i in range(n):
    mapp.append(list(map(str,input())))
    for j in range(m):
        if mapp[i][j] == 'R':
            rx, ry = i, j

        if mapp[i][j] == 'B':
            bx, by = i, j


#상하좌우 기울이기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q.append([rx,ry,bx,by,1])
visited.append([rx,ry,bx,by])



def move(x,y,i,j):
    count = 0
    while mapp[x+i][y+j] != '#' and mapp[x][y] != 'O':
        x+=i
        y+=j
        count += 1
    return x,y,count


def bfs():
    while q:
        rx,ry,bx,by,cnt = q.popleft()

        if cnt > 10:
            break
        for i in range(4):
            nrx, nry, rCnt = move(rx,ry,dx[i], dy[i])
            nbx, nby, bCnt = move(bx, by, dx[i], dy[i])

            if mapp[nbx][nby] == 'O':
                continue
            if mapp[nrx][nry] == 'O':
                return cnt
            if nrx == nbx and nry == nby:
                if rCnt > bCnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if [nrx, nry, nbx, nby] not in visited:
                visited.append([nrx, nry, nbx, nby])
                q.append([nrx, nry, nbx, nby, cnt + 1])
    return -1

print(bfs())