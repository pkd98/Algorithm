T = int(input())
idx = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b = map(int,input().split())
    if a < b:
        print(f"#{idx}",'<')
    elif a == b:
        print(f"#{idx}",'=')
    else:
        print(f"#{idx}",'>')
    idx += 1
