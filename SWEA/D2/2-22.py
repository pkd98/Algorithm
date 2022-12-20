'''
파리 퇴치

N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.
아래는 N=5 의 예이다.


M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
죽은 파리의 개수를 구하라!
예를 들어 M=2 일 경우 위 예제의 정답은 49마리가 된다.
'''
# N=5일때 M=2면, 완전 탐색 4*4씩 순회
# 즉, N-M+1 씩 순회
# 그 안에서 M*M번 크기 값 확인 -> 각 경우의 저장

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]
    answer = [[0 for _ in range(N-M+1)] for _ in range(N-M+1)]

    for i in range(N-M+1):
        for j in range(N-M+1):
            for x in range(M):
                for y in range(M):
                    answer[i][j] += area[x+i][y+j]
    print(f"#{tc}", max(map(max, answer)))