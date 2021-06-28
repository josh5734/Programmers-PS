from collections import deque

# bfs 탐색을 통해 각 노드까지의 거리 구하기
def bfs(n, graph, start):
    visited = [False] * (n+1)
    q = deque()
    
    # 맨 처음 노드의 거리 정보를 0으로 초기화하고 시작
    q.append((start,0))
    visited[start] = True
    distance = []
    while q:
        now, dist = q[0][0], q[0][1]
        q.popleft() 
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                # 다음 노드까지 거리는 현재 노드의 dist에서 1을 더한 값
                q.append((next,dist+1))
                distance.append((next, dist+1))
    
    # 거리 정보를 담는 리스트를 반환
    return distance

def solution(n, edge):
    # 엣지, 간선 정보 입력받기
    graph = [[] for _ in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    # 1번 노드부터 거리 정보를 담는 distance 리스트
    distance = bfs(n, graph, 1)
    
    # 최대 거리 값 구하기
    max_distance = sorted(distance, key = lambda x : -x[1])[0][1]
    
    # 최대 거리인 노드가 몇 개인지 구하기
    answer = 0
    for d in distance:
        if d[1] == max_distance:
            answer += 1
    return answer

