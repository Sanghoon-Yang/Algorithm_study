import copy

n,m = map(int, input().split())
mapp = []
magic_info = []
for _ in range(n):
    mapp.append(list(map(int, input().split())))

for _ in range(m):
    d,s = map(int, input().split())
    magic_info.append((d-1,s))

def empty_space(arr):
    tmp_arr = []
    for i in arr:
        if i != 0:
            tmp_arr.append(i)
    return tmp_arr

def explosion(arr):
    tmp_arr = []
    ans_1 = 0
    ans_2 = 0
    ans_3 = 0
    target = 0
    cnt = 0
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[target]:
            cnt += 1
            ball_num = arr[target]
        else:
            if cnt >= 4:
                for k in range(target, i,1):
                    arr[k] = 0
                if ball_num == 1:
                    ans_1 += cnt
                elif ball_num == 2:
                    ans_2 += cnt
                elif ball_num == 3:
                    ans_3 += cnt


            target = i
            cnt = 1


    return tmp_arr, ans_1, ans_2, ans_3


dx = [-1,1,0,0] # 상 하 좌 우
dy = [0,0,-1,1]
s_x, s_y = n//2, n//2

dx_s = [0,1,0,-1] # 좌 하 우 상
dy_s = [-1,0,1,0]
cnt = 0

mapp_in_a_row = []
mapp_in_a_row.append(mapp[s_x][s_y])
res_1 = 0
res_2 = 0
res_3 = 0

for magic in range(m):
    # 얼음 파편
    d,s = magic_info[magic]
    for r in range(s):
        nx = s_x + dx[d] * (r+1)
        ny = s_y + dy[d] * (r+1)
        if 0<=nx<n and 0<=ny<n:
            mapp[nx][ny] = 0

    # 빈칸 채우기 좌 하 우 상 순서 일열로 배치하기
    x, y = s_x, s_y
    for i in range(2*n-1):
        d = i%4
        if d == 0 or d == 2:
            cnt += 1
        #print(i)
        #print(cnt)
        for _ in range(cnt):

            nx = x + dx_s[d]
            ny = y + dy_s[d]
            if ny < 0:
                break
            else:
                mapp_in_a_row.append(mapp[nx][ny])
                x,y = nx,ny

        # 구슬 폭발
        while True:
            new_arr = empty_space(mapp_in_a_row)
            mapp_in_a_row, ans1, ans2, ans3 = explosion(new_arr)
            print(ans1, ans2, ans3)
            if ans1 == 0 and ans2 == 0 and ans3 == 0:
                break
            else:
                res_1 += ans1
                res_2 += ans2
                res_3 += ans3

print(res_1 + res_2*2+res_3*3)
        # 구슬 변화

