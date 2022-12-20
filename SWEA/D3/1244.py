'''
1244. [S/W 문제해결 응용] 2일차 - 최대 상금


퀴즈 대회에 참가해서 우승을 하게 되면 보너스 상금을 획득할 수 있는 기회를 부여받는다.

우승자는 주어진 숫자판들 중에 두 개를 선택에서 정해진 횟수만큼 서로의 자리를 위치를 교환할 수 있다.

예를 들어, 다음 그림과 3, 2, 8, 8, 8 의 5개의 숫자판들이 주어지고 교환 횟수는 2회라고 하자.


정해진 횟수만큼 숫자판 교환 -> 받을 수 있는 가장 큰 금액 계산
'''
# 숫자 - 주어진 횟수만큼 자리수 변경
# 정해진 횟수 N 만큼 교환하고 최대 금액 구하기
# N번의 모든 교환 경우의수 탐색 ->
# 가장 큰 값 도출

#DFS - 백트래킹 풀이
#교환 횟수만큼의 dfs 수행

def dfs(n):
    global answer
    #재귀 종료 조건 - 0부터 N까지 모두 탐색됨.
    if n == N:
        #int형 리스트의 원소들을 합친 후, 더 큰 값 최대값 갱신
        answer = max(answer, int("".join(map(str, lst))))
        return

    #총 L개의 번호에서 2개를 뽑아 서로 교환하는 모든 조합(경우의수)
    for i in range(L-1):
        for j in range(i+1, L):
            lst[i], lst[j] = lst[j], lst[i] #자리 교환
            # 변경된 리스트 값 저장
            lst_check = int("".join(map(str, lst)))
            # 해당 방문횟수와 리스트 값에 대해
            # 가보지 않은 새로운 길이면 방문.
            # 이미 가봤던 길이면, 방문하지 않게되어 중복이 제거된다.
            if (n, lst_check) not in visited:
                dfs(n+1)
                visited.append((n, lst_check))
                #방문 추가를 재귀호출이 완료된 이후
                #재귀 호출이 끝나고 return 되는 과정에서 한다.
                # 88832인 경우 첫번째 두번째 88인 경우 완료 하고
                # 두번째 세번째 88 교환하는 과정까지 막아버리면 안된다.
                # 따라서 dfs 트래킹 과정을 끝내고 돌아오는 중에 막아야 된다.
            lst[i], lst[j] = lst[j], lst[i] #dfs 백트래킹 이후, 다시 원상 복구


T = int(input())
for tc in range(1,T+1):
    nums, N = input().split() #숫자판, 교환횟수
    N = int(N)
    lst = []
    #리스트에 숫자판을 자리수별로 넣음
    for i in nums:
        lst.append(int(i))
    L = len(lst)
    visited = []
    answer = 0 # 최대 값 초기화
    dfs(0) #0번 교환 부터 ~ N번 교환까지 DFS를 이용한 백트래킹 수행
    print(f"#{tc}", answer)