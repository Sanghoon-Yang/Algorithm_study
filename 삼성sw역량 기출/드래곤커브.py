n = int(input())


def turn(dir):
    return (dir + 1) % 4

def dragon_curve(d,g):
    dir_info = []

    dir_info.append(d)
    for i in range(g):

        short_dir = []
        for j in range(len(dir_info)):
            k = len(dir_info) - (j + 1)
            d = dir_info[k]
            nd = turn(d)
            short_dir.append(nd)

        dir_info.extend(short_dir)
    return dir_info

def square(x,y):
    b1,b2 = x-1,y
    c1,c2 = x, y+1
    d1,d2 = x-1,y+1
    return [(b1,b2), (c1,c2), (d1,d2)]


dx = [1,0,-1,0]
dy = [0,-1,0,1]

coord_list = []

for _ in range(n):
    x,y,d,g = map(int, input().split())
    dir_info = dragon_curve(d,g)
    for d in dir_info:
        nx = x+dx[d]
        ny = y+dy[d]
        #if (nx,ny) not in coord_list:
        coord_list.append((nx,ny))
        x,y = nx,ny
print(set(coord_list))
result = 0
for x,y in coord_list:
    square_list = square(x,y)
    a = 0
    print((x,y))
    for p,q in square_list:
        if (p,q) in coord_list:
            print((p,q))
            a += 1
    print(a)
    if a == 3:
        result += 1
        print('checked')
print(result)
