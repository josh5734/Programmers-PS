def solution(triangle):
    height = len(triangle)

    for i in range(1, height):  # 아래 대각선으로 가면서 누적합
        for j in range(i+1):
            if j == 0:  # 왼쪽 끝 자리
                triangle[i][j] += triangle[i-1][j]
            elif j == i:  # 오른쪽 끝자리
                triangle[i][j] += triangle[i-1][j-1]
            else:  # 그 외에는 위의 양측 대각선 중 큰 값과 자기자신을 합
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    return max(triangle[-1])  # 맨 아래층에서 최대값


if __name__ == "__main__":
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    result = solution(triangle)
    print(result)
