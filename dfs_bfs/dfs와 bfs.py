from collections import deque


def dfs(v):

    visited[v] = True

    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

if __name__=='__main__':
    n, m, v = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(len(graph)):
        graph[i].sort()

    visited = [False] * (n+1)
    dfs(v)
    print()
    visited = [False] * (n + 1)
    bfs(v)