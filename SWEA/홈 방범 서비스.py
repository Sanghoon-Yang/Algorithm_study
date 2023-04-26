def dfs(x,y,depth,k):
    global cnt, visited, ans
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    if depth == k:
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and mapp[nx][ny] == 1 and visited[nx][ny] == 0:
            cnt += 1
            visited[nx][ny] = 1
            dfs(nx, ny, depth+1, k)
            visited[nx][ny] = 0




T = int(input())
for tc in range(T):
    n,m = map(int,input().split())
    mapp = []
    house_list = []
    for i in range(n):
        mapp.append(list(map(int, input().split())))
        for j in range(n):
            if mapp[i][j] == 1:
                house_list.append((i,j))
    ans = 0
    # for 루프 안에서 초기화 해주면서
    for k in range(1, n+2):
        for x in range(n):
            for y in range(n):
                cnt = 0
                for hx,hy in house_list:
                    dist = abs(hx-x)+abs(hy-y)
                    if dist < k:
                        cnt += 1
                if cnt * m >= k**2 + (k-1)**2:
                    ans = max(ans, cnt)



    print('#{} {}'.format(tc+1, ans))
