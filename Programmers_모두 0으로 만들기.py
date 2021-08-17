from collections import defaultdict

def dfs(tree, a, start, visited):
    print(a, visited)

    global answer
    # 상쇄할 가중치를 answer에 더한다.
    weight = a[start]
    a[start] -= weight
    answer += abs(weight)
    visited[start] = True

    # 현재 노드로부터 가장 먼 노드에게 가중치를 전달
    for next in tree[start]:
        if not visited[next]:
            a[next] += weight
            dfs(tree, a, next, visited)
    print("end")


answer = 0
def solution(a, edges):
    # 가중치를 상쇄할 수 없으면 -1 리턴
    if sum(a) != 0:
        return -1

    # 연결 정보를 담는 트리
    tree = defaultdict(list)
    for edge in edges:
        sour, dest = edge
        tree[sour].append(dest)
        tree[dest].append(sour)

    # 연결된 정점의 가중치가 0이라도, 이어진 다른 정점과 연쇄적으로 가중치가 상쇄 가능
    # Ex) node = [3, 10, 0, -5, -5, -3], edges = [[0,1],[0,2],[1,3],[1,4],[2,5]]
    length = len(a)
    visited = [False] * length
    dfs(tree, a, 0, visited)


    return answer 
    
a = [-5,0,2,1,2]
edges = [[0,1],[3,4],[2,3],[0,3]]

a2 = [0,1,0]
edges2=	[[0,1],[1,2]]

x = [3, 10, 0, -5, -5, -3]
x2 = [[0,1],[0,2],[1,3],[1,4],[2,5]]
print(solution(a,edges))


