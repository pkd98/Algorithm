# N-Queen 1차원 배열로 풀기
# 1차원 배열: index- 행, 해당 데이터 값- 열
# (퀸들의 위치를 비교)
# 같은 행인지, 같은 열인지, 대각선 상에 같이 있는지만 알면되기 때문에 2차원 배열이 필요없다.

'''
1. 각 테스트 케이스마다 dfs() 함수를 호출하여 result 값을 구하여 해당 테스트 케이스 번호와 함께 출력한다.

2. dfs() 함수의 작업은 아래와 같다.
  - 만약 전달받은 cnt 값과 입력받은 N이 같을 경우 마지막 행까지 퀸을 다 놓은 것이므로 result 값을 1 증가시킨 후 반환한다.
  - N개의 0으로 초기화된 temp 리스트를 정의한다.
  - arr 리스트의 값을 하나씩 꺼내 해당 값을 temp 리스트의 인덱스로 하여 1로 갱신한다.
  - 왼쪽 대각선, 오른쪽 대각선 또한 범위를 벗어나지 않는다면 해당 위치를 1로 갱신한다.
  - temp 리스트 요소를 순서대로 확인하면서 해당 인덱스의 값이 0이라면 dfs() 함수를 재귀호출한다.
  - 이때 arr 리스트에 해당 인덱스를 포함시키고, cnt 값을 1 증가시켜 전달한다.
'''

def dfs(arr, cnt) :
    global N, answer
    print('arr',arr)
    #종료 조건 - cnt(놓은 퀸 갯수), N 같으면 종료.
    if cnt == N:
        answer += 1
        return
    #열을 판단하기 위한 temp 배열.
    temp = [0] * N

    for i in range(len(arr)):
        #행은 어차피 못옴 1차원 배열 인덱스 이미 쓰고있음.
        # 열
        temp[arr[i]] = 1 #temp 인덱스가 열번호가 되고, 해당 열에는 못놓음.
        # 왼쪽 대각선
        if arr[i] - (cnt - i) >= 0: # 범위 내에 있다면
            temp[arr[i] - (cnt-i)] = 1
        # 오른쪽 대각선
        if arr[i] + (cnt - i) < N: # 범위 내에 있다면
            temp[arr[i] + (cnt-i)] = 1

    for i in range(N):
        if temp[i] == 0: # 빈 칸이라면,
            print('temp',temp)
            #temp의 인덱스가 열 값이므로, arr에 해당 열에 퀸을 놓고 다시 dfs를 부른다.
            dfs(arr + [i], cnt + 1)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cnt = 0  # dfs 호출 횟수 기록
    answer = 0
    dfs([], 0)

    print(f"#{tc}", answer)
