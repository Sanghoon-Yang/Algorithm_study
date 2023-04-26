n = int(input())
sand = []
for _ in range(n):
    sand.append(list(map(int, input().split())))
ans = 0
sx,sy = n//2, n//2
left = [[2,0,0.01],[1,1,0.01],[1,-0,0.07],[1,-1,0.1],[0,-2,0.05],
        [-1,1,0.01],[-1,0,0.07],[-1,-1,0.1],[-2,0,0.02],[0,-1,0]]
down = [[-y,x,z] for x,y,z in left]
right = [[x,-y,z] for x,y,z in left]
up = [[y,x,z] for x,y,z in left]

def count_sand(s_x,s_y,direction):
    global ans

    if sy < 0:
        return

    total = 0
    for dx,dy,r in direction:
        nx = s_x + dx
        ny = s_y + dy

        if r == 0:
            new_sand = sand[s_x][s_y] - total
        else:
            new_sand = int(sand[s_x][s_y] * r)
            total += new_sand
        if 0<=nx<n and 0<=ny<n:
            sand[nx][ny] += new_sand
        else:
            ans += new_sand

dx = [0,1,0,-1]
dy = [-1,0,1,0]

dict = {0:left, 1:down, 2:right, 3:up}
time = 0

for i in range(2*n-1):
    d = i%4
    if d == 0 or d == 2:
        time += 1
    for _ in range(time):
        n_x = sx + dx[d]
        n_y = sy + dy[d]
        count_sand(n_x,n_y, dict[d])
        sx,sy = n_x,n_y

print(ans)

