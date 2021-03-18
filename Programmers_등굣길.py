def show(graph):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            print(graph[i][j], end=' ')
        print()


def solution(m, n, puddles):
    graph = [[0] * m for _ in range(n)]
    graph[0][0] = 1  # 시작 위치
    for x, y in puddles:
        graph[y-1][x-1] = -1  # 물 웅덩이

    dx, dy = [1, 0], [0, 1]  # 오른쪽과 아래 방향
    for x in range(n):
        for y in range(m):
            if graph[x][y] != -1:
                for i in range(2):
                    nx, ny = x+dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != -1:
                        graph[nx][ny] += graph[x][y]
    return graph[n-1][m-1] % 1000000007


if __name__ == "__main__":
    m, n = 6, 3
    puddles = [[1, 3], [2, 2]]
    result = solution(m, n, puddles)
    print(result)
