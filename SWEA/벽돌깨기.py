def delete_block(x,y):
    cnt = board[x][y]
    board[x][y] = 0
    if cnt > 1:
        for i in range(1,cnt):
            for dx, dy in delta:
                nx = x + dx * i
                ny = y + dy * i
                if 0<=nx<h and 0<= ny < w:
                    if board[nx][ny] > 1:
                        delete_block(nx,ny)
                    board[nx][ny] = 0

def gravity():
    new_board = [[0]*w for _ in range(h)]
    for wi in range(w):
        init = h-1
        for j in range(h-1, -1,-1):
            if board[h][w]:
                new_board[init][w] = board[h][w]
                init -= 1
    return new_board
