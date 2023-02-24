year = int(input())

a=year%4==0
b=year%100!=0
c=year%400==0

if a :
    if c or b:
        print("1")
    else : print("0")
else : print("0")