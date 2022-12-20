'''
N-Quenn

N*N 체스보드 N개의 퀸
서로다른 두 퀸이 공격하지 못하게 놓는 경우의 수 출력

'''

'''
중복 제거/ 도중에 다시 들어가야되는 경우. 구현 못함..
'''
# 첫번째 자리 부터 퀸 놓기 -> 못놓는 곳 0 초기화
# 가능한 자리 중 가까운 자리에 두번째 퀸 놓기
# => DFS 이용 탐색

# 퀸 - 좌우상하 대각선 공격 => (0) 또는 visited에 방문 설정?
# ex) 1000
#     0011
#     0101
#     0110
#
# DFS 수행 -> 1찾기 -> 1찾으면 해당자리 방문 표시와 함께 다시 좌우상하, 대각선 방문 표시
# (재귀적 반복)

# [왼쪽 방향을 갖는 대각선들의 규칙]
#
# (1, 1)(2, 2)(3, 3)...  -> 모두
# x - y = 0
#
# (1, 2)(2, 3)(3, 4)...  -> 모두
# x - y = -1
#
# [오른쪽 방향을 갖는 대각선들의 규칙]
#
# (5, 1)(4, 2)(3, 3)...   -> 모두
# x + y = 6
#
# (4, 1)(3, 2)(2, 3)...   -> 모두
# x + y = 5


def dfs(x, y):
    global answer
    global cnt # dfs 호출 수 (퀸을 놓은 수)
    cnt += 1
    check = set()
    #######################################초기화###########################################
    # 시작점 0 초기화 (방문처리)
    graph[x][y] = 0
    # 퀸 위치 - 공격 범위 0 초기화
    # 좌
    for i in range(1, N):
        if y - i < 0:
            break
        else:
            graph[x][y - i] = 0
    # 우
    for i in range(1, N):
        if y + i > N - 1:
            break
        else:
            graph[x][y + i] = 0
    # 상
    for i in range(1, N):
        if x - i < 0:
            break
        else:
            graph[x - i][y] = 0
    # 하
    for i in range(1, N):
        if x + i > N - 1:
            break
        else:
            graph[x + i][y] = 0
    # 대각선 \ : i==j, / :x-i+y+j==x+y or x+i+y-j==x+y
    for i in range(N):
        for j in range(N):
            if not (x+i > N-1 or y+j > N-1):
                if i == j:
                    graph[x + i][y + j] = 0
            if not (x-i < 0 or y-j < 0):
                if i == j:
                    graph[x-i][y-i] = 0
            if not (x-i <0 or y+j > N-1):
                if (x-i)+(y+j) == x+y:
                    graph[x-i][y+j] = 0
            if not (x+i > N-1 or y-j < 0):
                if (x+i)+(y-j) == x+y:
                    graph[x+j][y-j] = 0
############################################################################################################


    #####디버깅######
    for i in range(N):
        print('카운트', cnt)
        print(graph[i])
    print()
    #################

    #그래프 체크
    for i in range(N):
        for j in range(N):
            check.add(graph[i][j])

    # 종료조건 - 놓을 자리가 없음 return
    if 1 not in check:
        check.clear()
        if cnt == N:
            answer += 1
        return

    # 1인 경우에 dfs 수행
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                temp = []
                temp.extend(graph)
                dfs(i, j)
                graph.clear()
                graph.extend(temp)





T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    graph = [[1] * N for _ in range(N)]
    cnt = 0  # dfs 호출 횟수 기록
    answer = 0

    for i in range(N):
        for j in range(N):
            dfs(i, j)
            graph = [[1] * N for _ in range(N)]
            #print(cnt)
            cnt = 0

    print(f"#{tc}", answer)




    # # 좌
    # for i in range(1, N):
    #     if y - i < 0:
    #         break
    #     else:
    #         graph[x][y - i] = 0
    # # 우
    # for i in range(1, N):
    #     if y + i > N - 1:
    #         break
    #     else:
    #         graph[x][y + i] = 0
    # # 상
    # for i in range(1, N):
    #     if x - i < 0:
    #         break
    #     else:
    #         graph[x - i][y] = 0
    # # 하
    # for i in range(1, N):
    #     if x + i > N - 1:
    #         break
    #     else:
    #         graph[x + i][y] = 0


    # #그래프 체크
    # for i in range(N):
    #     for j in range(N):
    #         check.add(graph[i][j])