A, B = map(int,input().split())
# A = (A+1)%3
# B = (B+1)%3

# A이기는 경우 : (1,3),(2,1),(3,2)
# B이기는 경우 : (1,2),(2,3),(3,1)


if A < B:
    if A+1 == B:
        print("B")
    if (B+1)%3 == 0:
        print("B")

elif A > B:
    if B+1 == A:
        print("A")
    if (A+1)%3 == 0:
        print("A")
