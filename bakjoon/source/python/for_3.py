n=int(input())
m=[]
sum = 0

for i in range(0,n):
    m.append(n-i)
    sum = sum + m[i]
print(sum)