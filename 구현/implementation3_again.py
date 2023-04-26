n,m = map(int,input().split())

maps = []
d = [[0] *m for _ in range(n)]

x, y, dir = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3

for i in range(n):
    map_row = list(map(int, input().split()))
    maps.append(map_row)

count = 1
turn_count = 0
while True:
    turn_left()
    nx = x + dx[dir]
    ny = y + dy[dir]

    if d[nx][ny] == 0 or maps[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_count = 0
        continue
    else:
        turn_count += 1

    if turn_count == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]

        if maps[nx][ny] == 0:
            x = nx
            y = ny

        else:
            break
        turn_count = 0

print(count)