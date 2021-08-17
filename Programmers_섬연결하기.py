import heapq
# Minimum Spanning Tree 문제


def solution(n, costs):
    answer = 0
    graph = [[] for _ in range(n)]

    for x, y, cost in costs:  # 인접리스트 형태로 입력받기
        graph[x].append((y, cost))
        graph[y].append((x, cost))

    visited = [False] * n  # 방문 표시 테이블
    pq = []  # 우선순위 큐를 이용해서 간선의 비용이 적은 것부터 고려
    heapq.heappush(pq, (0, 0))  # 시작점 삽입
    count = 0
    while count < n:  # 방문해야 하는 정점의 수만큼 반복
        cost, start = heapq.heappop(pq)
        if not visited[start]:
            visited[start] = True  # 방문 처리
            count += 1
            answer += cost
            for dest, cost in graph[start]:
                if not visited[dest]:
                    # 튜플의 0번째 원소를 cost로 해서 pq 삽입
                    heapq.heappush(pq, (cost, dest))
    return answer


if __name__ == "__main__":
    n = 4
    costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
    answer = solution(n, costs)
    print(answer)
