'''
파스칼의 삼각형

크기가 N인 파스칼의 삼각형을 만들어야 한다.

파스칼의 삼각형이란 아래와 같은 규칙을 따른다.
1. 첫 번째 줄은 항상 숫자 1이다.
2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.

N이 4일 경우,
N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pascal = [[0] * N for _ in range(N)]
    pascal[0][0] = 1

    print(f"#{tc}")
    print(pascal[0][0])

    for i in range(1, N):
        for j in range(N):
            if j == 0:
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

            if pascal[i][j] != 0:
                print(pascal[i][j], end=' ')

        print('')
