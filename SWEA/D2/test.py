li = [2, 2, 2, 1,1,1,1,1,2,3,1,1]
max_count = 0
count = 0
for i in range(0, len(li)-1):
    if li[i] == li[i+1]:
        count += 1
        print(count)
    else:
        if max_count < count:
            max_count = count
            max_num = li[i]
            count = 0
print(str(max_num) + "가 " + str(max_count) + "번연속으로 나왔습니다.")