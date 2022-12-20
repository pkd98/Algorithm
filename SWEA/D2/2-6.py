'''
0 : 현재 속도 유지.
1 : 가속
2 : 감속

가속(1) 또는 감속(2) 의 경우 가속도의 값이 추가로 주어진다.

가속도의 단위는, m/s2 이며, 모두 양의 정수로 주어진다.

입력으로 주어진 N 개의 command 를 모두 수행했을 때, N 초 동안 이동한 거리를 계산하는 프로그램을 작성하라.

RC 카의 초기 속도는 0 m/s 이다.
'''

T = int(input())
for tc in range(1,T+1):
    distance = 0  # 거리 = 속도*시간
    velocity = 0  # 속도
    N = int(input()) #커맨드 갯수

    for i in range(N):
        command = list(map(int, input().split()))

        if command[0] == 0:
            distance += velocity #sec는 1이므로, 거리 = 1*속도
        else:
            if command[0] == 1:
                velocity += command[1] #가속
                distance += velocity

            elif command[0] == 2:
                velocity -= command[1]
                if velocity < 0:
                    velocity = 0
                distance += velocity
    print(f"#{tc}", distance)
