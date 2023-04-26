import copy
from collections import deque



def bfs(x,y, arr):
    visited = [[0]*n for _ in range(n)]
    route_list = [[0]*n for _ in range(n)]
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    route_list[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0 and arr[nx][ny] <= arr[x][y]:
                q.append((nx,ny))
                visited[nx][ny] = 1
                route_list[nx][ny] = route_list[x][y] + 1
            else:
                continue
    max_length = 0
    for i in range(n):
        for j in range(n):
            max_length = max(max_length, route_list[i][j])

    return max_length

if __name__=='__main__':
    t = int(input())

    for test in range(t):
        n, k = map(int, input().split())
        val = -1e9
        mountain = []
        for i in range(n):
            mountain.append(list(map(int, input().split())))
            for j in range(n):
                val = max(mountain[i][j], val)

        highest = []
        for i in range(n):
            for j in range(n):
                if mountain[i][j] == val:
                    highest.append([i, j])

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        max_length_total = 0
        for x, y in highest:
            for i in range(n):
                for j in range(n):
                    if (i,j) != (x,y):
                        for exp in range(0, k+1):
                            mountain_tmp = copy.deepcopy(mountain)
                            mountain_tmp[i][j] = mountain[i][j] - exp

                            max_length = bfs(x,y, mountain_tmp)
                            max_length_total = max(max_length_total, max_length)



        print('#{} {}'.format(t+1, max_length_total))



