
def dfs(x,y):
    if x < 0 or x >=4 or y < 0 or y >= 4 or mapp[x][y] != 1:
        return
    mapp[x][y] = 0
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y +1)



if __name__=='__main__':
    mapp = []
    for i in range(4):
        mapp.append(list(map(int, input())))

    result = 0
    for i in range(4):
        for j in range(4):
            if mapp[i][j] == 1:
                dfs(i,j)
                result += 1
    print(result)