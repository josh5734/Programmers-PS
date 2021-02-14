def dfs(n, start, visited, computers):
    # 시작 위치를 방문 체크하고
    visited[start] = True
    for i in range(n):
        # 연결된 노드에 대해
        if computers[start][i] == 1:
            # 아직 방문하지 않았다면
            if visited[i] == False:
                # 다시 dfs를 수행
                dfs(n, i, visited, computers)
    # dfs가 종료되면 True를 반환
    return True


def solution(n, computers):
    answer = 0
    # 방문을 체크할 테이블 생성
    visited = [False] * n

    for i in range(n):
        # 아직 방문하지 않은 노드에 대해 dfs수행
        if visited[i] == False:
            if dfs(n, i, visited, computers) == True:
                answer += 1
    return answer


if __name__ == "__main__":

    n = 3
    computers = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print(solution(n, computers))
