'''
스도쿠 검증
입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때,
위와 같이 겹치는 숫자가 없을 경우,
1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.

'''
T = int(input())

for tc in range(1, T+1):
    #스도쿠 9*9 2차원 배열 저장
    sudoku = [list(map(str,input().split())) for _ in range(9)]
    offset_row = [0, 0, 0, 3, 3, 3, 6, 6, 6] # 3*3 격자 검증을 위한 시작 주소
    offset_col = [0, 3, 6, 0, 3, 6, 0, 3, 6]
    state = True

    #1. 각 가로줄 검증
    for i in range(9):
        checker = set(sudoku[i])
        if len(checker) != 9:#검증 실패
            state = False
            break

    #2. 각 세로줄 검증
    for i in range(9):
        row = [s[i] for s in sudoku] #세로줄 한줄
        checker = set(row)
        if len(checker) != 9: #검증 실패
            state = False
            break

    #3. 3*3 격자 검증
    for idx in range(9): #3*3 격자 9개
        checker = set()
        for i in range(3): #한 격자 만큼 검증
            for j in range(3):
                checker.add(sudoku[i+offset_row[idx]][j+offset_col[idx]])
        if len(checker) != 9:#검증 실패 0출력
            state = False
            break

    #검증 모두 통과 1출력
    print(f"#{tc}",1) if state == True else print(f"#{tc}", 0)