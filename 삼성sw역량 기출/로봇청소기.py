from collections import deque

n,m = map(int, input().split())
# robot
x,y,d = map(int, input().split())

def turn(d):
    return (d-1)%4

mapp = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    mapp.append(list(map(int, input().split())))

visited = [[False]*m for _ in range(n)]


visited[x][y] = True
ans = 1
turn_count = 0
while True:
    d = turn(d)
    nx = x + dx[d]
    ny = y + dy[d]

    if 0<=nx<n and 0<=ny<m and visited[nx][ny] == False and mapp[nx][ny] == 0:
        visited[nx][ny] = True
        ans += 1
        turn_count = 0
        x,y = nx,ny
        continue

    else:
        turn_count += 1

    if turn_count == 4:
        nx = x - dx[d]
        ny = y - dy[d]

        if mapp[nx][ny] == 0:
            x,y = nx,ny
        else:
            break
        turn_count = 0

print(ans)

