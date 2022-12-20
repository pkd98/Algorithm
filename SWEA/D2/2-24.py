'''
패턴 마디의 길이
패턴에서 반복되는 부분을 마디라고 부른다. 문자열을 입력 받아 마디의 길이를 출력하는 프로그램을 작성하라.

각 문자열의 길이는 30이다. 마디의 최대 길이는 10이다.

'''
# 처음 문자와 같은 문자가 다시 나올경우, 쭉쭉 판독 시작
# 다르면 판독X 다시 첫글자 같은거 나오면 판독 시작

T = int(input())
for tc in range(1, T+1):
    str = input()
    word = ""

    for i in range(1, 30):
        # 첫 글자가 다시 나오면, 해당 번호만큼 다시 반복해서 word에 넣음.
        if str[i] == str[0]:
            for j in str[i:i+i]:
                word += j
        #마디 찾으면 출력하고 멈춤
        if word == str[:i]:
            print(f"#{tc}", len(word))
            break
        #틀리면, 다시 word 초기화
        else:
            word = ""
