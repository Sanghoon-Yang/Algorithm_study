n = int(input())
k = int(input())
apple = [[0]*(n+1) for _ in range(n+1)]

for _ in range(k):
    a,b = map(int, input().split())
    apple[a][b] = 1

l = int(input())
dir_var = []
for _ in range(l):
    x,c = input().split()
    dir_var.append((int(x), str(c)))


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(direction, c):
    if c == 'L':
        direction = (direction-1)%4
    elif c == 'D':
        direction = (direction+1)%4
    return direction

def solution():
    x = 1
    y = 1
    direction = 0
    time = 0
    apple[x][y] = 2
    index = 0
    tail = [(x,y)]

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if nx >= 1 and nx <= n and ny >= 1 and ny <= n and apple[nx][ny] != 2:
            if apple[nx][ny] == 1:
                apple[nx][ny] = 2
                tail.append((nx,ny))
                qx, qy = tail.pop(0)
                apple[qx][qy] = 0
            elif apple[nx][ny] == 1:
                tail.append((nx,ny))
                apple[nx][ny] = 2
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if time == dir_var[index][0]:
            direction = turn(direction, dir_var[index][1])
            index += 1
    return time

if __name__=='__main__':
    print(solution())