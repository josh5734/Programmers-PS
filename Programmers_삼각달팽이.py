
def show(triangle):
    for i in range(len(triangle)):
        row = triangle[i]
        for r in row:
            print(r, end=" ")
        print()


def solution(n):
    # 각 행에는 각 행의 번호만큼의 숫자를 저장할 수 있음
    triangle = [[] for _ in range(n)]
    for i in range(n):
        triangle[i] = [0 for _ in range(i+1)]

    # 시작 숫자 = 1, 시작 방향은 위에서 왼쪽 아래 방향
    number = 1
    startDirection = "topToBottom"
    init_idx = 0  # 각 행에서 달팽이가 숫자를 입력할 때 앞에서부터 입력하는지 뒤에서부터 입력하는지 체크하기 위한 변수
    start, end = 0, n  # 처음 시작 idx, 끝 idx 설정(꼭대기, 바닥)

    while number <= n*(n+1) / 2:  # number = n(n+1) / 2가 되면 모든 칸이 채워진 것
        # 위에서 왼쪽 아래로 가는 경우
        if startDirection == "topToBottom":
            # 왼쪽 대각선 IDX부터 차례대로 채워나감
            for i in range(start, end):
                triangle[i][init_idx] = number
                number += 1
            init_idx += 1
            start += 1
            startDirection = "bottomToBottom"  # 방향 체인지

        # 밑바닥을 지나는 경우
        if startDirection == "bottomToBottom":
            startIdx = init_idx
            # 밑바닥에 0이 없을때까지 쭉 채워나감
            while(triangle[end-1].count(0) != 0):
                triangle[end-1][startIdx] = number
                number += 1
                startIdx += 1
            end -= 1
            startDirection = "bottomToTop"  # 방향 체인지

        # 오른쪽 아래에서 위로 가는 경우
        if startDirection == "bottomToTop":
            # 오른쪽 바깥 대각선 인덱스 방향으로 채워져 올라감
            for i in range(end-1, start-1, -1):
                triangle[i][i-init_idx+1] = number
                number += 1
            start += 1
            startDirection = "topToBottom"  # 방향 체인지
    answer = []

    # 정답 리스트에서 출력
    for i in range(len(triangle)):
        row = triangle[i]
        for r in row:
            answer.append(r)
    return answer


if __name__ == "__main__":
    n = 7
    print(solution(n))
