#P: A사의 1리터당 P원의 요금
#Q : B사 기본요금
#R: 월간 사용량 R리터 이하일때 기본요금
#S: R리터 넘을때 1리터당 S원 추가요금
#W: 종민이 한달 사용 수도양

#P, Q, R, S, W(1 ≤ P, Q, R, S, W ≤ 10000, 자연수)
#요금 저렴한 회사를 골라서 그 요금 계산
T = int(input())
price = 0
for tc in range (1,T+1):
    P, Q, R, S, W = map(int, input().split())
    A_price = P*W
    B_price_over = Q+(W-R)*S
    #요금 더 저렴한 회사 고르기 -> 그회사 계산
    if R >=W: #B사 사용량 기본요금
        if A_price < Q:
            #A사 요금 계산 출력
            print(f'#{tc}', A_price)
        else:
            #B사 요금 계산 출력
            print(f'#{tc}', Q)

    else: #B사 초과요금
        if A_price < B_price_over:
            #A사 요금 계산 출력
            print(f'#{tc}', A_price)
        else:
            #B사 요금 계산 출력
            print(f'#{tc}', B_price_over)

