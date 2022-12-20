#첫번째 N번 양세기
#두번째 2N번 양세기
#k번째 kN번 양세기
#이전에 셋던 번호들의 각 자리수에서 0~9까지 모든 숫자를 보는 것은 최소 몇번의 양을 센 시점?

#set 집합에 각 자리수 넣음 (.update([]))
#튜플 0~9완성되면 횟수 카운트 리턴 양세기 종료


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    N_set = set([])
    k=1

    while(True):
        Num = N*k
        str_N = str(Num)
        str_N_len = len(str_N)

        for i in str_N:
            N_set.add(i)

        if len(N_set) == 10:
            break
        k += 1
    print(f"#{test_case}", Num)