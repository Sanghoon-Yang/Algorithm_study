from collections import deque
n,m,k,x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

result = [[] for _ in range(n+1)]
info = [-1]*(n+1)
info[x] = 0

q = deque()
q.append(x)

while q:
    a = q.popleft()

    for node in graph[a]:
        if info[node] == -1:
            info[node] = info[a] + 1
            q.append(node)

check = False
for i in range(i, n+1):
    if info[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)








