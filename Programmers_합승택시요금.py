def show(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            print(graph[i][j], end=' ')
        print()


def floyd(n, fares):
    inf = int(1e9)

    graph = [[inf] * (n+1) for _ in range(n+1)]
    # 자기 자신에서 자기 자신으로 가는 비용 = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0

    # 각 간선에 대한 비용 정보 입력
    for fare in fares:
        start, end, cost = fare
        graph[start][end] = cost
        graph[end][start] = cost

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

    return graph


def solution(n, s, a, b, fares):
    answer = 0
    # 플로이드 워셜로 모든 지점에서 모든 지점으로 가는 비용을 계산
    graph = floyd(n, fares)
    show(graph)

    # 두 사람이 합승해서 가는 도착지를 노드 N이라고 하면 최종 요금은 (시작 -> N) * 1/2 + 각 사람이  N -> 도착점까지 가는 비용
    min_cost = (1e9)
    for together in range(1, n+1):
        cost = graph[s][together] + graph[together][a] + graph[together][b]
        if cost < min_cost:
            min_cost = cost
    return min_cost


if __name__ == "__main__":
    n, s, a, b = 6, 4, 6, 2
    fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [
        5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
    print(solution(n, s, a, b, fares))
