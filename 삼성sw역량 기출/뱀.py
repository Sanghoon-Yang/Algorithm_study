n = int(input())
k = int(input())

mapp = [[0]*(n+1) for _ in range(n+1)]
dir_var = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(k):
    a,b = map(int, input().split())
    mapp[a+1][b+1] = 1


l = int(input())

turns = dict()
for _ in range(l):
    s, d = input().split()
    turns[int(s)] = 1 if d == "D" else -1
# for _ in range(l):
#     a,b = input().split()
#     dir_var.append([int(a),b])


def solution():
    x,y = 1,1
    mapp[x][y] = 2
    direction = 0
    time = 0
    q = [(x,y)]

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if nx >= 1 and ny >= 1 and nx <=n and ny <=n and mapp[nx][ny] != 2:
            if mapp[nx][ny] == 0:
                mapp[nx][ny] =2
                q.append((nx, ny))
                qx, qy = q.pop(0)
                mapp[qx][qy] = 0

            if mapp[nx][ny] == 1:
                mapp[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        x,y = nx, ny
        time += 1

        if time in turns:
            direction = (direction + turns[time]) % 4
    return time


print(solution())