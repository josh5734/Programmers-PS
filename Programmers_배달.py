import heapq
inf = int(1e10)
def dijkstra(start, graph, N, K):
    distance = [inf] * (N+1)
    distance[1] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        # 현재 노드를 꺼낸다.
        dist, now = heapq.heappop(q)
        if dist < distance[now]:
            continue
        # 현재 노드에서 다른 노드까지 비용 갱신
        for nodeIndex, cost in enumerate(graph[now]):
            if distance[nodeIndex] > cost + dist:
                distance[nodeIndex] = cost + dist
                q.append((cost + dist, nodeIndex))
    answer = 0
    print(distance)
    for d in distance:
        if d <= K:
            answer += 1
    return answer 

def solution(N, road, K):
    graph = [[inf] * (N+1) for _ in range(N+1)]
    # 그래프의 거리 정보 초기화
    for sour, dest, cost in road:
        if cost < graph[sour][dest]:
            graph[sour][dest] = cost
            graph[dest][sour] = cost

    # 자기 자신까지 가는 거리는 0으로 초기화
    for i in range(1, N+1):
        graph[i][i] = 0
    return dijkstra(1, graph, N, K)

print(solution(N=6, road=[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],K=4))