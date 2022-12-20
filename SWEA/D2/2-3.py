#N명 사람 돌던지기
#원하는 지점에 최대한 가깝게 돌던지기
#밀리 미터 단위 -100,000~100,000
#1000,000에 써있는 위치에서 최대한 0에 가까운 위치로 돌던지기
#N명 사람들이 던진 돌 떨어진 위치 측정 자료 주어짐

#가장 0에 가깝게 떨어진 위치 주어짐
# -> 0사이의 거리 차이
# -> 몇명이 그렇게 돌을 던졌는지

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    pos = list(map(int,input().split()))
    pos_len = len(pos)

    for i in range(pos_len):
        if pos[i] < 0:
            pos[i] = -pos[i]

    min_pos = min(pos)
    min_count = pos.count(min_pos)

    print(f"#{tc}", min_pos, min_count)