from collections import deque

inf = int(1e10)





def dijkstra(start, graph, N, K):
    distance = [inf] * (N+1)
    distance[1] = 0

    q = deque()
    q.append((0, start))

    while q:
        # 현재 노드를 꺼낸다.
        dist, now = q.popleft()

        # 현재 노드에서 다른 노드까지 비용 갱신
        for next in range(1, N+1):
            cost = dist + graph[now][next]

            if distance[next] > cost:
                distance[next] = cost
                q.append((cost, next))
    answer = 0
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


'''
def dijkstra(start, graph, N, K):
    
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    answer = 0
    for d in graph[1]:
        if d <= K: 
            answer += 1
    return answer
'''