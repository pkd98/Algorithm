'''
지그재그 숫자

1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.

N이 5일 경우,
1 – 2 + 3 – 4 + 5 = 3

N이 6일 경우,
1 – 2 + 3 – 4 + 5 – 6 = -3

'''
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    answer = 0
    for i in range(1,N+1):
        if i % 2: #홀수
            answer += i
        else:
            answer -= i

    print(f"#{tc}", answer)