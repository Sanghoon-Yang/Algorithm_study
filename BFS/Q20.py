from collections import deque
from itertools import combinations
from copy import deepcopy

n = int(input())

mapp = []
empty_list = []
teacher = []

for i in range(n):
    mapp.append(list(input().split()))
    for j in range(n):
        if mapp[i][j] == 'X':
            empty_list.append((i,j))
        if mapp[i][j] == 'T':
            teacher.append((i,j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]




def gamsy(x,y, mapp):
    result = 0
    for i in range(4):

        for _ in range(n):

            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if mapp[nx][ny] == 'X':
                    mapp[nx][ny] = 'T'
                    x = nx
                    y = ny
                elif mapp[nx][ny] == 's':
                    result += 1
                    x = nx
                    y = ny
                elif mapp[nx][ny] == 'O':
                    break
    return result

wall_list = combinations(empty_list,3)
q = deque(teacher)

for wall in wall_list:
    temp = deepcopy(mapp)

    for i,j in wall:
        temp[i][j] = 'O'

    while q:
        x,y = q.popleft()

        result = gamsy(x,y, temp)
print(temp)
print(result)







