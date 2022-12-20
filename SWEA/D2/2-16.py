'''
시각 덧셈

시 분으로 이루어진 시각을 2개 입력 받아, 더한 값을 시 분으로 출력하는 프로그램을 작성하라.
(시각은 12시간제로 표시한다. 즉, 시가 가질 수 있는 값은 1시부터 12시이다.)

시는 1 이상 12 이하의 정수이다. 분은 0 이상 59 이하의 정수이다.

'''

T = int(input())

for tc in range(1,T+1):
    h1,m1,h2,m2 = map(int,input().split())
    time = [h1+h2,m1+m2]

    if time[1] >= 60:
        time[0] += 1
        time[1] -= 60

    if time[0] > 12:
        time[0] -= 12

    print(f"#{tc}", time[0], time[1])
