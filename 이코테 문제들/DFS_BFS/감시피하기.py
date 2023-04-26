#NXN크기의 복도가 있음
#특정한 위치에는 선생님 학생 장애물 존재
#각 선생님은 상하좌우 방향으로 감시를 진행
# 장애물이 있으면 장애물 뒤편은 볼 수 없음
# 장애물을 정확히 3개를 설치하여 학생들 모두가 감시를 피할 수 있는지 출력하는 프로그램 작성.
import copy
from itertools import combinations
n = int(input())
graph = []
teacher = []
student = []
empty = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    graph.append(list(input().split()))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'S':
            student.append([i,j])
        elif graph[i][j] == 'T':
            teacher.append([i,j])
        else:
            empty.append([i,j])


def dfs(temp,x,y):
    global cnt
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<n and temp[nx][ny] != 'O':
            if temp[nx][ny] == 'S':
                cnt += 1
            temp[nx][ny] = 'T'
            dfs(temp, nx, ny)





cand = combinations(empty, 3)

check = 0
for c in cand:
    temp = copy.deepcopy(graph)
    cnt = 0
    for wx,wy in c:
        temp[wx][wy] = 'O'

    for x,y in teacher:
        dfs(temp,x,y)

    if cnt == 0:
        print('YES')
        break
    else:
        check += 1

if check != 0:
    print('NO')

