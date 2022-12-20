'''
중간 평균값 구하기

10개의 수를 입력 받아, 최대 수와 최소 수를 제외한 나머지의 평균값을 출력하는 프로그램을 작성하라.
(소수점 첫째 자리에서 반올림한 정수를 출력한다.)

'''
T = int(input())

for tc in range(1,T+1):
    nums = list(map(int, input().split()))
    nums.remove(max(nums)) #remove는 중복되면 하나만 지움.
    nums.remove(min(nums))
    print(f"#{tc}", round(sum(nums)/8))