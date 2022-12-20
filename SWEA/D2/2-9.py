#날짜 계산기
'''
월 일로 이루어진 날짜를 2개 입력 받아,
두 번째 날짜가 첫 번째 날짜의 며칠째인지 출력하는 프로그램을 작성하라.

월은 1 이상 12 이하의 정수이다. 각 달의 마지막 날짜는 다음과 같다.

1/31, 2/28, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31

두 번째 날짜가 첫 번째 날짜보다 항상 크게 주어진다.
'''

T = int(input())
month_end = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for tc in range(1, T+1):
    date = list(map(int, input().split()))
    month_diff = date[2] - date[0]
    answer = 0
    idx = 0

    if month_diff == 0:
        print(f'#{tc}',date[3] - date[1] + 1)
        continue

    idx = date[0] - 1
    answer += month_end[idx] - date[1]

    for i in range(1,month_diff):
        idx = date[0]+i-1
        answer += month_end[idx]

    answer += date[3]+1

    print(f'#{tc}', answer)


#깔끔한 코드
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for tc in range(1, int(input())+1):
    m1, d1, m2, d2 = map(int, input().split())
    ans = 0

    # 같은 달에 위치할 경우
    if m1 == m2:
        ans = d2 - d1 + 1

    else:
        # 시작하는 달
        ans = months[m1] - d1 + 1
        # 중간에 있는 달
        for i in range(m1 + 1, m2):
            ans += months[i]
        # 마지막 달
        ans += d2
    print(f'#{tc} {ans}')