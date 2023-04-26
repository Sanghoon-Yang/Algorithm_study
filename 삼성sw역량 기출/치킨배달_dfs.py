n,m = map(int, input().split())
city = []
house = []
chicken = []
choosen_chicken = []
for i in range(n):
    city.append(list(map(int, input().split())))
    for j in range(n):
        if city[i][j] == 1:
            house.append([i,j])
        elif city[i][j] == 2:
            chicken.append([i,j])

ans = 1e9

def combination(depth, idx):
    global ans
    if depth == m:
        sum = 0
        for h in house:
            val = 1e9
            for chick in choosen_chicken:
                length = abs(h[0] - chick[0]) + abs(h[1]-chick[1])
                val = min(length,val)
            sum += val
        ans = min(ans, sum)
        return

    for i in range(idx, len(chicken)):
        if chicken[i] in choosen_chicken:
            continue
        choosen_chicken.append(chicken[i])
        combination(depth+1, i+1)
        choosen_chicken.pop()

combination(0,0)
print(ans)