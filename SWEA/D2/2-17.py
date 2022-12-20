'''
N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.
주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.

'''
T = int(input())

# 퍼즐 한 행씩, 연속된 가로 1갯수 K개 찾기
def findContinuous_1(puzzle, N, K):
    answer = 0

    for i in range(N):
        cnt = 1
        for j in range(0, N-1):
            if puzzle[i][j] == puzzle[i][j+1] == 1:
                cnt += 1
            else:
                if cnt == K:
                    answer += 1
                cnt = 1
        if cnt == K:
            answer += 1
    return answer


for tc in range(1,T+1):
    N, K = map(int, input().split()) #N*N 퍼즐, K크기 단어
    puzzle = [list(map(int, input().split())) for _ in range(N)] #검은부분:0, 흰부분:1
    puzzle_T = list(zip(*puzzle))

    cnt = findContinuous_1(puzzle, N , K)
    cnt += findContinuous_1(puzzle_T, N, K)

    print(f"#{tc}", cnt)




    # for i in range(N):
    #     for j in range(0, N-1):
    #         if puzzle[i][j] == puzzle[i][j+1] == 1:
    #             cnt[i] += 1
    #             print(cnt)
    #         else:
    #             if cnt[i] == K:
    #                 continue
    #             cnt[i] = 1
    #
    # #퍼즐 한 열씩, 연속된 세로 1갯수 K개 찾기
    # for i in range(N):
    #     for j in range(0, N-1):
    #         if puzzle_T[i][j] == puzzle_T[i][j+1] == 1:
    #             cnt[i] += 1
    #             print(cnt)
    #         else:
    #             if cnt[i] == K:
    #                 continue
    #             cnt[i] = 1