
def solution(routes):
    # 차량이 한 대밖에 없으면 1을 리턴
    if len(routes) == 1:
        return 1
    # 차량의 대수는 1이상으로 카메라를 한 개로 초기화
    camera = 1
    # 진입 시점이 작은 순서대로 정렬
    routes = sorted(routes, key=lambda x: (x[0], x[1]))
    # 현재 카메라의 위치
    curr = routes[0][1]
    for i in range(1, len(routes)):
        start, end = routes[i][0], routes[i][1]
        # 마지막 카메라의 위치보다 진입 시점이 앞에 있으면 curr 변경
        if start <= curr:
            curr = min(curr, end)
        # 마지막 카메라의 위치보다 늦게 진입하면 카메라를 더 설치해야 함
        if start > curr:
            camera += 1
            curr = end
    return camera


if __name__ == "__main__":
    routes = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
    routes2 = [[0, 1], [1, 2], [2, 3], [3, 4], [3, 3]]
    routes3 = [[-30000, -30000], [30000, 30000], [10000, 30000]]
    routes4 = [[0, 10], [2, 8], [3, 9]]
    answer = solution(routes2)
    print(answer)
