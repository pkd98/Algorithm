#인코딩 하기
'''
24bit 버퍼에 MSB 부터 한바이트씩 3바이트 문자 넣음
버퍼의 위쪽부터 6비트씩 잘라 그 값 읽은 후 표1 문자로 인코딩

디코딩 해서 원문 출력하기

문자열 길이 항상 4의 배수
문자열 길이 100000 안넘음 (10만)
'''

#6비트 잘린 값 4개 모아서 24비트
# - > 8byte로 다시 잘라서 디코딩

T = int(input())

for tc in range(1,T+1):
    B64_str = str(input())
    Binary_B64 = "" #입력값 2진수 형태로 저장할 변수
    answer = ""
    for i in B64_str:
        if i.isupper(): #대문자 A -> 0시작
            Binary_B64 += format(ord(i) - ord('A'),'b').zfill(6) #해당 문자->int 형 변환-> 6bit길이 2진수로

        elif i.islower(): #소문자 a -> 26시작
            Binary_B64 += format(ord(i) - ord('a') + 26,'b').zfill(6)

        elif i.isdigit():#숫자 0 -> 52시작
            Binary_B64 += format(ord(i) - ord('0') + 52,'b').zfill(6)

        elif i == '+':
            Binary_B64 += format(62,'b').zfill(6)

        elif i == '/':
            Binary_B64 += format(63,'b').zfill(6)

    for i in range(0,len(Binary_B64),8): #8bit씩 잘라서 아스키코드 문자로 변환
        answer += chr(int(Binary_B64[i:i+8],2)) #자른 8bit를 해당 아스키코드로 변환

    print(f'#{tc}',answer)