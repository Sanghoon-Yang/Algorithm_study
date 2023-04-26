import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
mapp = []
for _ in range(n):
    mapp.append(list(map(int, input().split())))

command = list(map(int, input().split()))

dx = [0,0,-1,1]
dy = [1,-1,0,0]


def turn(dir,dice):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    elif dir == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    elif dir == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e


dice_arr = []
for i in command:
    nx = x + dx[i-1]
    ny = y + dy[i-1]
    if nx <0 or ny <0 or nx >= n or ny >=m:
        continue
    # if mapp[nx][ny] == 0:
    #
    # if mapp[nx][ny] != 0:

    x,y = nx, ny
