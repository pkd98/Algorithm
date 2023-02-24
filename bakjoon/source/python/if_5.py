H, M =  map(int,input().split())

if M>=45:
    M=M-45
    print(H, M)
elif H>0 and M<45:
    H=H-1
    M=M+60-45
    print(H, M)
elif H==0 and M<45:
    H=H+24-1
    M=M+60-45
    print(H, M)