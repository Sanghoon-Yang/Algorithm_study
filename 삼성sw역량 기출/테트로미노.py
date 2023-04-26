import sys
input = sys.stdin.readline

def dfs(depth, summ,x,y):
    global val
    if depth == 4:
        val = max(val, summ)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(depth +1, summ + mapp[nx][ny], nx,ny)
            visited[nx][ny] = 0



def exce(x,y):
    global val
    dir_list = [[0,2,3],[0,1,3],[1,2,3],[0,1,2]]
    for dir in dir_list:
        tmp = mapp[x][y]
        for k in dir:
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= n or ny <0 or ny >= m:
                tmp = 0
                break
            tmp += mapp[nx][ny]
        val = max(val, tmp)




if __name__=='__main__':
    n, m = map(int, input().split())
    mapp = []
    val = 0
    for _ in range(n):
        mapp.append(list(map(int, input().split())))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[0]*m for _ in range(n)]

    for x in range(n):
        for y in range(m):
            visited[x][y] = 1
            dfs(1,mapp[x][y],x,y)
            visited[x][y] = 0

            exce(x,y)

    print(val)


