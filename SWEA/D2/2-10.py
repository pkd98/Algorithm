
T = int(input())

for tc in range(1,T+1):
    size = int(input())
    snail = [[0]*size for _ in range(size)] #달팽이 2차원 배열 생성
    direction = 0  # 우:0, 하:1, 좌:2, 상:3
    num_fill = size #해당하는 한 방향으로 채우는 숫자 개수 설정.

    row, col = 0,-1 #좌표 초기값

    dr = [0,1,0,-1] #우,하,좌,상 : 방향에 따른 row값 변화량
    dc = [1,0,-1,0] #col 변화량

    num = 0
    while num < size*size : # 2차원 배열 값 넣을 만큼 반복
        #한 방향 채우기
        for _ in range(num_fill):
            row += dr[direction]
            col += dc[direction]
            num += 1
            snail[row][col] = num

        direction += 1 #다음 방향을 위해 방향값 변화

        if direction % 4 == 0: #방향 초기화
            direction = 0

        if direction % 2:
            num_fill -= 1

    print(f"#{tc}")
    for i in range(size):
        print(*snail[i])
