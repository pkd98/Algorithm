'''
N 개의 숫자로 구성된 숫자열 Ai (i=1~N)
M 개의 숫자로 구성된 숫자열 Bj (j=1~M)

마주보는 숫자 곱한뒤 모두 더할때 최대값 구하기
더 긴쪽의 양 끝 벗어나면 안됨

N 과 M은 3 이상 20 이하이다.

'''

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    #1. 배열 나누기
    if N<M:
        min_li = Ai
        max_li = Bj
    else:
        min_li = Bj
        max_li = Ai

    loop = len(max_li)-len(min_li)+1
    value = [0]*loop

    #2. 움직여보면서 마주보는 수 곱하고 더하고 계산
    for i in range(loop):
        for j in range(len(min_li)):
            value[i] += min_li[j]*max_li[i+j]

    print(value)

    #3. 더 큰 값 프린트
    print(f"#{tc}", max(value))