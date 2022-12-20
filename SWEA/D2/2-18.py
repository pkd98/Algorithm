'''
조교의 성적 매기기

A+ ~ D0 (10개의 평점)
중간/기말 결과 및 과제 점수 반영

[중간 35, 기말 45, 과제 20]

예를 들어, N 명의 학생이 있을 경우 N/10 명의 학생들에게 동일한 평점을 부여할 수 있다.
입력으로 각각의 학생들의 중간, 기말, 과제 점수가 주어지고,
학점을 알고싶은 K 번째 학생의 번호가 주어졌을 때,
K 번째 학생의 학점을 출력하는 프로그램을 작성하라.

'''
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(N)]
    total = []
    #각 평점당 같은 비율 부여. 각 평점당 N/10 비율로 부여함.

    #scores를 각 비율별 총점 합계 리스트 만들기
    for i in range(N):
        total.append(scores[i][0]*0.35 + scores[i][1]*0.45 + scores[i][2]*0.2)

    #K번째 학생에 대한 등수를 통해 무슨 학점인지 판단
    K_score = total[K-1]
    total.sort(reverse=True)
    K_rank = total.index(K_score) + 1

    print(f"#{tc}", end=" ")
    if K_rank <= N/10:
        print("A+")
    elif K_rank <= 2*N//10:
        print("A0")
    elif K_rank <= 3*N//10:
        print("A-")
    elif K_rank <= 4*N//10:
        print("B+")
    elif K_rank <= 5*N//10:
        print("B0")
    elif K_rank <= 6*N//10:
        print("B-")
    elif K_rank <= 7*N//10:
        print("C+")
    elif K_rank <= 8*N//10:
        print("C0")
    elif K_rank <= 9*N//10:
        print("C-")
    elif K_rank <= 10*N//10:
        print("D0")

# #다른사람 짧은 코드
# for t in range(int(input())):
#     N, K = map(int,input().split())
#     r=[[*map(int,input().split())]for _ in range(N)]
#
#     k = r[K-1]
#     r.sort(key=lambda x:.35*x[0]+.45*x[1]+.2*x[2]);
#
#     print(f"#{t+1} {['D0','C-','C0','C+','B-','B0','B+','A-','A0','A+'][r.index(k)//(N//10)]}")