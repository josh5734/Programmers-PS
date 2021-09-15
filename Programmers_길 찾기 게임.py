from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)


def preOrder(tree, root, route):
    route.append(root)

    left, right = tree[root][0], tree[root][1]
    if left != -1:
        preOrder(tree, left, route)
    if right != -1:
        preOrder(tree,right, route)

    return route

def postOrder(tree, root, route):
    left, right = tree[root][0], tree[root][1]
    if left != -1:
        postOrder(tree, left, route)
    if right != -1:
        postOrder(tree,right, route)
    route.append(root)

    return route

def makeTree(tree, nodeDict, root, node):
    x, y = nodeDict[node][0], nodeDict[node][1]

    while True:
        rootX, rootY = nodeDict[root][0], nodeDict[root][1]
        # 왼쪽 서브트리에 삽입
        if rootX > x:
            if tree[root][0] == -1:
                tree[root][0] = node
                break
            else:
                root = tree[root][0]

        # 오른쪽 서브트리에 삽입
        else:
            if tree[root][1] == -1:
                tree[root][1] = node
                break
            else:
                root = tree[root][1]
            

def solution(nodeinfo):
    answer = [[],[]]
    nodeList = defaultdict(list)
    for idx, node in enumerate(nodeinfo):
        nodeList[idx+1] = node

    # Root부터 왼쪽, 오른쪽 순서로 내려오는 노드 형태로 정렬
    nodeList = sorted(nodeList.items(), key = lambda x: (-x[1][1], x[1][0]))
    root = nodeList[0][0]
    nodeDict = dict(nodeList)


    # 트리의 왼쪽, 오른쪽 자식 노드의 인덱스를 -1로 초기화
    tree = defaultdict(list)
    for i in range(1, len(nodeinfo)+1):
        tree[i] = [-1,-1]

    for i in range(1, len(tree)):
        makeTree(tree, nodeDict, root, nodeList[i][0])

    # 순회 경로를 위한 빈 리스트를 매개변수로 초기화하고 함수 콜
    answer[0] = preOrder(tree, root, [])
    answer[1] = postOrder(tree, root, [])

    return answer


print(solution(nodeinfo=[[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
# print(solution(nodeinfo=[[5,5],[4,4],[3,3],[2,2],[1,1]]))
# print(solution(nodeinfo=[[1,1],[2,2],[3,3]]))