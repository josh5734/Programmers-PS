from collections import deque
    
        
def solution(board):
    count = 0
    N = len(board)
    p1, p2 = [0,0],[0,1]    # 시작점
    visited = []    # 방문을 체크할 배열
    
    dx, dy = [1,-1,0,0],[0,0,1,-1]  # 상하좌우 이동
    
    q = deque() # 큐 생성
    q.append([p1,p2,"H",0])    # [[0,0],[0,1],"H",0]
    visited.append([p1,p2,"H"])  # 방문 체크
    
    while q:
        current = q.pop()
        x1,y1,x2,y2,status, count = current[0][0], current[0][1], current[1][0], current[1][1],current[2], current[3]
        if [x1,y1] == [N-1,N-1] or [x2,y2] == [N-1,N-1]:
            return count
        # 상하좌우 이동에 대하여
        for i in range(4):
            nx1,ny1,nx2,ny2 = x1 + dx[i], y1 + dy[i], x2 + dx[i], y2 + dy[i]
            # board 범위 안에 있고
            if (0 <= nx1 < N and 0 <= ny1 < N and 0 <= nx2 < N and 0 <= ny2 < N):
                # 이동하려는 곳이 벽이 아니고
                if(board[nx1][ny1] == 0 and board[nx2][ny2] == 0):    
                    # 방문을 한 적이 없다면
                    if [[nx1,ny1],[nx2,ny2],status] not in visited:
                        visited.append([[nx1,ny1],[nx2,ny2],status])
                        q.append([[nx1,ny1],[nx2,ny2],status,count+1])

        # 회전에 대하여
        if status == "H":
            # 위 방향 회전 가능
            if (0 <= x1 - 1 and board[x1-1][y1] == 0 and board[x2-1][y2] == 0):
                if [[x1-1,y1],[x1,y1],"V"] not in visited:
                    visited.append([[x1-1,y1],[x1,y1],"V"])
                    q.append([[x1-1,y1],[x1,y1],"V",count+1])
                if [[x2-1,y2],[x2,y2],"V"] not in visited:
                    visited.append([[x2-1,y2],[x2,y2],"V"])
                    q.append([[x2-1,y2],[x2,y2],"V",count+1])
                    
            # 아래 방향 회전 가능
            if (x1 + 1 < N and board[x1+1][y1] == 0 and board[x2+1][y2] == 0):
                if [[x1,y1],[x1+1,y1],"V"] not in visited:
                    visited.append([[x1,y1],[x1+1,y1],"V"])
                    q.append([[x1,y1],[x1+1,y1],"V",count+1])
                if [[x2,y2],[x2+1,y2],"V"] not in visited:
                    visited.append([[x2,y2],[x2+1,y2],"V"])
                    q.append([[x2,y2],[x2+1,y2],"V",count+1])
                    
        if status == "V":
            # 왼쪽 부분 회전
            if (0 <= y1 - 1 and board[x1][y1-1] == 0 and board[x2][y2-1] == 0):
                if [[x1,y1-1],[x1,y1],"H"] not in visited:
                    visited.append([[x1,y1-1],[x1,y1],"H"])
                    q.append([[x1,y1-1],[x1,y1],"H",count+1])
                if [[x2,y2-1],[x2,y2],"H"] not in visited:
                    visited.append([[x2,y2-1],[x2,y2],"H"])
                    q.append([[x2,y2-1],[x2,y2],"H",count+1])
            # 오른쪽 부분 회전
            if (y1 + 1 < N and board[x1][y1+1] == 0 and board[x2][y2+1] == 0):
                if [[x1,y1],[x1,y1+1],"H"] not in visited:
                    visited.append([[x1,y1],[x1,y1+1],"H"])
                    q.append([[x1,y1],[x1,y1+1],"H",count+1])
                if [[x2,y2],[x2,y2+1],"H"] not in visited:
                    visited.append([[x2,y2],[x2,y2+1],"H"])
                    q.append([[x2,y2],[x2,y2+1],"H",count+1])