directions = [(1, -1), (1, 1), (-1, 1), (-1, -1)]

def dfs(i, j, dir, cnt):
    global answer

    if dir < 3:
        tmp = dir + 2
    else:
        tmp = dir + 1
    for k in range(dir, tmp):
        ni = i + directions[k][0]
        nj = j + directions[k][1]
        if start[0] == ni and start[1] == nj:
            answer = max(answer, cnt)
            return
        if 0 <= ni < n and 0 <= nj < n:
            if cafe_visited[ni][nj] == False and dessert_visited[arr[ni][nj]] == False:
                cafe_visited[ni][nj] = True
                dessert_visited[arr[ni][nj]] = True

                dfs(ni, nj, k, cnt + 1)

                cafe_visited[ni][nj] = False
                dessert_visited[arr[ni][nj]] = False

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for x in range(n)]

    cafe_visited = [[False]*n for x in range(n)]
    dessert_visited = [False] * 101
    answer = -1

    for i in range(n-2):
        for j in range(1, n-1):
            start = (i, j)
            cafe_visited[i][j] = True
            dessert_visited[arr[i][j]] = True

            dfs(i, j, 0, 1)
            cafe_visited[i][j] = False
            dessert_visited[arr[i][j]] = False
    print(f'#{t} {answer}')