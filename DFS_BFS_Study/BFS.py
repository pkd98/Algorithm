from collections import deque

def bfs(graph, start, visited):
    #큐 구현을 위해 deque 라이브러리 사용. 시작 노드 초기화
    queue = deque([start])
    #현재 노드를 방문 처리
    visited[start] = True
    #큐가 비어 있을 때 까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        #아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

#각 노드가 방문된 정보를 표현
visited = [False] * 9

bfs(graph, 1, visited)