'''
미로 탈출

N*M 직사각형 형태의 미로에 갇힘
시작 위치 (1,1) - 가장 왼쪽 위. 탈출구 (N,M). 한번에 한번씩 이동 가능
괴물이 있는 부분은 0, 없는 부분은 1. 미로는 반드시 탈출 가능 형태 제시.

탈출하기 위해 최소 이동 개수를 구하라. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산.

ex)
5 6
101010
111111
000001
111111
111111   -> 10 출력.
'''
from collections import deque

def bfs (x, y):
    #큐 구현 및 처음 시작 노드 넣음
    queue = deque()
    queue.append((x, y))
    #큐가 비어있을 때 까지 반복
    while queue:
        x, y = queue.popleft()
        #현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            #미로 공간 벗어난 경우 무시
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
                continue
            #벽인 경우 무시
            if graph[next_x][next_y] == 0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[next_x][next_y] == 1:
                graph[next_x][next_y] = graph[x][y] + 1
                queue.append((next_x, next_y))
    # 가장 오른쪽 아래까지의 최단거리 반환
    return graph[N-1][M-1]


N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

#이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#BFS 수행 결과 출력
print(bfs(0,0))