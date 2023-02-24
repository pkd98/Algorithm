A,B=map(int,input().split())
C=int(input())

B=B+(C%60)

if B>=60:
    A=A+1
    B=B-60

A=(A+(C//60))%24

print(A, B)