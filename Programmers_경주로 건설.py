import heapq
from collections import deque

inf = int(1e9)
def dijkstra(board, init_right, direction):
    if direction == 0:
        board[0][1] = 1
    else:
        # 위에서 바꿨던 오른쪽 값을 초기값으로 세팅
        board[0][1] = init_right
        board[1][0] = 1

    n = len(board)
    dx, dy = [1,0,0,-1], [0,1,-1,0]
    distance = [[inf] * n for _ in range(n)]
    distance[0][0] = 0

    q = deque()
    preX, preY = 0, 0
    q.append((0, 0, 0 , preX, preY))
    
    while q:
        currCost, currX, currY,  preX, preY = q.popleft()
        for i in range(4):
            nx, ny = currX + dx[i], currY + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                if preX == nx or preY == ny:
                    newCost = currCost + 100
                else:
                    newCost = currCost + 600
                
                if newCost <= distance[nx][ny]:
                    q.append((newCost, nx, ny, currX, currY))
                    distance[nx][ny] = newCost
    return distance[n-1][n-1]             
        

def solution(board):
    answer = 0
    n = len(board)
    init_right = board[0][1]

    # 아래로 내려가는 방향과 오른쪽으로 가는 방향 둘 중에 최소값을 선택
    distance = min(dijkstra(board, init_right, 0), dijkstra(board, init_right,1))
    return distance

print(solution(board=[[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]]))