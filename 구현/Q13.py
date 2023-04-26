from itertools import combinations


n,m = map(int, input().split())
mapp = []
chicken_pos = []
house_pos = []

for i in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)

for i in range(n):
    for j in range(n):
        if mapp[i][j] == 1:
            house_pos.append((i,j))
        elif mapp[i][j] == 2:
            chicken_pos.append((i,j))




total = []
for i in combinations(chicken_pos, m):
    dis = 0
    for j in range(len(house_pos)):
        distance = []
        for k in range(len(i)):
            hx,hy = house_pos[j][0], house_pos[j][1]
            cx,cy = i[k][0], i[k][1]
            dist = abs(hx-cx) + abs(hy-cy)
            distance.append(dist)
        dis += min(distance)
    total.append(dis)

print(min(total))