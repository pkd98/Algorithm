#1. 최빈수 출력 - Counter() 이용
from collections import Counter

T = int(input())

for test_case in range(1, T + 1):
    idx = int(input())
    scores = list(map(int,input().split()))
    c = Counter(scores).most_common()[0][0] #Counter 최빈값 내림차순 나열, 최빈값 튜블 [0][0] 가장 큰 수 출력

    print(f"#{idx}",c)


# 2. 딕셔너리 이용
T = int(input())

for tc in range(1, T+1):
    idx = int(input())
    scores = list(map(int, input().split()))
    freq = {}
    for v in scores:
        freq.setdefault(v,0)
        freq[v] += 1
    freq_num, mode_freq = max(freq.items(), key=lambda x:x[1])
    print(f"#{idx}",freq_num)


#3. 정석 배열 이용
T = int(input())
for i in range(1, T + 1):
    num = input()
    arr = list(map(int, input().split()))
    num_arr = [0 for _ in range(101)]

    for el in arr: #점수 값을 토대로 배열에 최빈값 카운트 값 갱신
        num_arr[el] += 1

    max_num = 0
    idx = 0

    for el in range(len(num_arr)):
        if max_num <= num_arr[el]: #최빈값 max_num에 넣음
            max_num = num_arr[el]
            idx = el #최빈값에 해당하는 점수

    print("#" + num, idx)