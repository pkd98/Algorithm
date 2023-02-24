inputNum=int(input())
cnt=0
num=inputNum

while 1:
    A=num//10
    B=num%10
    C=(A+B)%10
    num=(B*10)+C
    
    cnt+=1

    if(num==inputNum):
        break

print(cnt)


##str로 구하기
#
#inputNum=input()
#num=inputNum
#cnt=0
#while 1:
#   if len(num) == 1:
#       num = '0'+num
#   plus = str(int(num[0]) + int(num[1]))
#   num = num[-1] * plus[-1]
#   cnt += 1
#   if num == inputNum:
#   print(cnt)
#    break