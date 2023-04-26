from collections import deque





def find_group(x,y,color):

    num_block = 1
    num_rainbow = 0
    block_pos = [[x,y]]
    rainbow_pos = []
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0 and blocks[nx][ny] == color:

                num_block +=1
                visited[nx][ny] = 1
                block_pos.append([nx,ny])
                q.append([nx,ny])
            elif 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0 and blocks[nx][ny] == 0:
                num_block += 1
                num_rainbow += 1
                rainbow_pos.append([nx,ny])
                q.append([nx,ny])
                visited[nx][ny] = 1

    for a,b in rainbow_pos:
        visited[a][b] = 0

    return [num_block, num_rainbow, block_pos + rainbow_pos]



def remove(block_info):
    for i,j in block_info:
        blocks[i][j] = -2


def rot90(arr):
    new_arr = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_arr[n-1-j][i] = arr[i][j]
    return new_arr

def gravity(arr):
    for c in range(n):
        for r in range(n-2, -1, -1):
            if arr[r][c] > -1:
                while True:
                    if 0<=r+1<n and arr[r+1][c] == -2:
                        arr[r+1][c] = arr[r][c]
                        arr[r][c] = -2
                        r+=1
                    else:
                        break
    return arr



if __name__=='__main__':
    n, m = map(int, input().split())
    blocks = []
    for _ in range(n):
        blocks.append(list(map(int, input().split())))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    score = 0
    while True:
        visited = [[0] * n for _ in range(n)]
        block_info = []

        for i in range(n):
            for j in range(n):
                color = blocks[i][j]
                if color > 0 and visited[i][j] == 0:
                    inform = find_group(i,j,color)
                    if inform[0] >= 2:
                        block_info.append(inform)
                else:
                    continue

        block_info.sort(reverse=True)
        if not block_info:
            break

        remove(block_info[0][2])
        score += block_info[0][0]**2
        #print(blocks)

        #gravity
        blocks = gravity(blocks)
        #print(blocks)
        blocks = rot90(blocks)
        blocks = gravity(blocks)
        #gravity
    print(score)