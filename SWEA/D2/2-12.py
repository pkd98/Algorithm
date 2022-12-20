'''
N x N 행렬이 주어질 때,

시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.

출력의 첫 줄은 '#t'로 시작하고,
다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.
입력과는 달리 출력에서는 회전한 모양 사이에만 공백이 존재함에 유의하라.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    matrix = []

    # 반복하면서 2차원 N*N 리스트에 값 저장
    for i in range(N):
        matrix.append(list(map(int, input().split())))

    #90도, 180도 270도 회전 모양 출력 (한줄씩 같이)
    #90도 : 왼쪽 밑에서 위로 - 시작점: 좌하단
    #180도 : 오른쪽 밑에서 좌로 - 시작점 : 우하단
    #270도 : 오른쪽 위에서 아래로 - 시작점 : 우상단

    print(f"#{tc}")
    for i in range(N):
        # 출력할 좌표 초기화
        row = [N, 0, -1]
        col = [0, N, 0]

        for j in range(N):
            row[0] -= 1
            col[0] = i
            print(matrix[row[0]][col[0]], end="")
        print(" ",end="")

        for k in range(N):
            row[1] = N-1-i
            col[1] -= 1
            print(matrix[row[1]][col[1]], end="")
        print(" ",end="")

        for l in range(N):
            row[2] += 1
            col[2] = N-1-i
            print(matrix[row[2]][col[2]], end="")
        print("")