import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int, input().split())
mapp = []
house = []
chicken = []
for i in range(n):
    mapp.append(list(map(int, input().split())))
    for j in range(n):
        if mapp[i][j] == 1:
            house.append((i,j))
        if mapp[i][j] == 2:
            chicken.append((i,j))

chicken_arr = combinations(chicken,m)

result = []

for i in chicken_arr:
    city_chicken_len = 0
    chicken_len = 0
    for j in house:

        dist = []
        for k in i:
            d = abs(j[0]-k[0])+abs(j[1]-k[1])
            dist.append(d)
        chicken_len += min(dist)
    city_chicken_len += chicken_len
    result.append(city_chicken_len)

print(min(result))
