from collections import deque

n,k = map(int, input().split())
belt = []
belt.append(list(map(int, input().split())))

q = deque()
for i,j in enumerate(belt[0]):
    q.append([i+1, j])



cnt = 0
zero_count = 0
while True:
    if zero_count >= k:
        break
    i,j = q.popleft()
    j -= 1
    if j == 0:
        zero_count += 1
    q.appendleft([i,j])

    for _ in range(2*n):
        i,j = q.popleft()
        if j > 0:
            j -= 1
        if j == 0:
            zero_count += 1
        q.append([i,j])

    q.rotate(1)
    cnt +=1


print(cnt)