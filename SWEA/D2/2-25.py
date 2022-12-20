'''
간단한 3 6 9 게임
숫자 1부터 순서대로 말하되, 3 6 9 안말함. 대신 박수침. 박수는 369 갯수만큼 친다.

박수는 "-"로 출력
박수 두번은 "--"이다.
'''

def check369(num):
    strNum = str(num)
    count = 0
    for i in strNum:
        if i in ('3','6','9'):
            count += 1
    if count == 0:
        return num
    else:
        return "-"*count

N = int(input())
for i in range(1,N+1):
    print(check369(i),end=" ")