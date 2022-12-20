T = int(input())

for tc in range(1,T+1):
    N = int(input())
    nums = sorted(map(int, input().split()))
    print(f"#{tc}", *nums)