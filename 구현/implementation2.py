pos = input()
row = int(pos[1])
col = int(ord(pos[0])) - int(ord(pos[0])) + 1

n = 8
count = 0
paths = [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

for i in paths:
    newrow = row + i[0]
    newcol = col + i[1]

    if newcol < 1 or newrow <1 or newrow > n or newcol > n:
        continue
    else:
        count +=1

print(count)
