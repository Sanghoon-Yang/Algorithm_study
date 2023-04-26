def dfs(graph, v, visited):
    visited[v] = True #노드 v를 방문처리
    print(v, end=' ') #방문한 노트 v 출력
    for i in graph[v]: #graph의 v 노드에 연결된 노드(i)들 순서대로 확인
        if not visited[i]: #i가 방문되지 않았다면
            dfs(graph, i, visited) #재귀함수로 dfs 다시 시작 ㅋㅋ


from collections import deque


def bfs(graph, start, visited):
    queue = deque([start]) # 큐에 시작점 추가하고

    visited[start] = True # 시작점은 방문처리 함
    while queue: #큐가 빌때까지 while 문 돌림
        v = queue.popleft() # 큐에서 선입된 노드 v pop
        print(v)
        for i in graph[v]: #graph의 v와 연결된 노드들 (i)
            if not visited[i]: #i가 방문처리 안됐따면,
                queue.append(i) #큐에다가 집어넣기 ㅋㅋ
                visited[i] = True # 후에 방문처리
