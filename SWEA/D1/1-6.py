T = int(input())

a = str(T)
answer = 0
for i in range(4):
    digits = ord(a[i]) - ord('0')
    answer += digits
print(answer)

## 각 자리수에 대한 합을 ord() 이용