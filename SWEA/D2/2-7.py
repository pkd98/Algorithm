#간단한 소인수 분해
'''
N=2^a x 3^b x 5^c x 7^d x 11^e

N이 주어질 때 a, b, c, d, e 를 출력하라.
(N은 2 이상 10,000,000 이하이다.)

'''
def Factorization(N, div):
    cnt = 0
    while (N%div)==0:
        N = N // div
        cnt += 1
    return N, cnt

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    N, a = Factorization(N, 2)
    N, b = Factorization(N, 3)
    N, c = Factorization(N, 5)
    N, d = Factorization(N, 7)
    N, e = Factorization(N, 11)

    print(f"#{tc}", a, b, c, d, e)