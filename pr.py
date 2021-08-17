from collections import defaultdict
import sys
sys.setrecursionlimit(100000000)

answer = 0

def dfs(tree, a, visited, node):
    global answer
    visited[node] = True

    for child in tree[node]:
        if not visited[child]:
            # dfs로 리프노드까지 탐색
            leafWeight = dfs(tree, a, visited, child)
            
            a[node] += leafWeight
            answer += abs(leafWeight)

    return a[node]

def solution(a, edges):
    if sum(a) != 0:
        return -1

    # 정점과 연결된 edge의 개수가 1개인 것부터 그리디하게 수행
    n = len(a)      # 정점의 개수

    # 연결 정보를 담는 트리
    tree = defaultdict(list)
    for edge in edges:
        sour, dest = edge
        tree[sour].append(dest)
        tree[dest].append(sour)

    visited = [False] * n    
    dfs(tree, a, visited, 0)

    return answer
