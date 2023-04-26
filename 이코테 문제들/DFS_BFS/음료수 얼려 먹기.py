n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m: # 범위 벗어나는 즉시 종료
        return False
    if graph[x][y] == 0: # 현재 노드 방문 안했으면,
        graph[x][y] = 1 # 1로 바꾸면서 방문처리 조짐
        dfs(x-1,y) #재귀적으로 상하 좌우 모두 dfs 호출
        dfs(x, y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result = 0
#모든 노드에 대하여 dfs 함
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1


print(result)