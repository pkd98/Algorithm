'''
강변에 빌딩들이 옆으로 빽빽하게 밀집한 지역이 있다.
이곳에서는 빌딩들이 너무 좌우로 밀집하여, 강에 대한 조망은 모든 세대에서 좋지만 왼쪽 또는 오른쪽 창문을 열었을 때 바로 앞에 옆 건물이 보이는 경우가 허다하였다.
그래서 이 지역에서는 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다고 말한다.
빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.
아래와 같이 강변에 8채의 빌딩이 있을 때, 연두색으로 색칠된 여섯 세대에서는 좌우로 2칸 이상의 공백이 존재하므로 조망권이 확보된다. 따라서 답은 6이 된다.


빌딩 너무 좌우로 밀집. 좌우로 창문 열었을때 건물 보임
좌우 창문 열었을 때 양쪽 거리 2이상 확보될 떄 조망권 확보
빌딩 정보 주어짐.
조망권 확보된 세대의 수를 반환

가로 길이 1000이하
맨왼쪽 두칸, 오른쪽 두칸 건물X
빌딩 최대 높이 255

'''
#건물의 좌,우 높이 비교
#해당 건물당, 2이상 널널하면 조망권 count

for tc in range(1, 11):
    N = int(input()) #건물의 갯수
    heights = list(map(int, input().split())) #건물들 높이
    answer = 0 #조망권 확보된 세대 카운트

    #모든 건물 경우에 대해서,
    for i in range(2, N-2):
        left = 0
        right =0

        #해당 빌딩 왼쪽 두칸 비교 (해당 빌딩보다 작은만큼 조망권 확보)
        #왼쪽의 건물 두채중에 큰거 고름 -> 해당 빌딩에서 값 빼기 -> 왼쪽 조망권 확보된 세대
        if heights[i] >= heights[i-1] >= heights[i-2]:
            left = heights[i] - heights[i-1]

        if heights[i] >= heights[i-2] > heights[i-1]:
            left = heights[i] - heights[i-2]

        #오른쪽 두칸 비교
        #오른쪽 건물 두채중에 큰거 고름 -> 해당 빌딩에서 값 빼기 -> 오른쪽 조망권 확보된 세대
        if heights[i] >= heights[i + 1] >= heights[i + 2]:
            right = heights[i] - heights[i + 1]

        if heights[i] >= heights[i + 2] > heights[i + 1]:
            right = heights[i] - heights[i + 2]

        #왼쪽, 오른쪽 조망권 확보된 세대중에 더 작은거 고르기
        if left < right:
            answer += left
        else:
            answer += right

    print(f"#{tc}", answer)