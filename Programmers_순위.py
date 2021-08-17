def dfs(winner, graph, results, visited, winning_result):
    visited[winner] = True
    for loser in graph[winner]:
        if not visited[loser]:
            winning_result.append(loser)
            dfs(loser, graph, results, visited, winning_result)


def solution(n, results):
    # 각 선수가 승리한 사람을 기록한 그래프
    graph = [[] for _ in range(n+1)]

    for result in results:
        win, lose = result[0], result[1]
        graph[win].append(lose)

    result_board = [[[], []] for _ in range(n+1)]

    # dfs 수행하면서 각 사람이 이긴 사람을 리스트에 추가
    for i in range(1, n+1):
        visited = [False] * (n+1)
        winning_result = []
        dfs(i, graph, results, visited, winning_result)
        result_board[i][0] = winning_result

    answer = 0
    # 각 선수가 누구에게 패배했는지를 역으로 기록
    for i in range(1, n+1):
        for w in result_board[i][0]:
            result_board[w][1].append(i)

    # 각 사람이 이기고 진 결과 내용이 n-1개라면 순위 정하기 가능
    for i in range(1, n+1):
        if len(result_board[i][0]) + len(result_board[i][1]) == n-1:
            answer += 1

    return answer




n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))