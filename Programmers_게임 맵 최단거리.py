from collections import deque
dx, dy = [1,-1,0,0], [0,0,1,-1]


def bfs(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)] 

    q = deque()
    q.append((0,0))
    visited[0][0] = True

    while q:
        curr_x, curr_y = q.popleft()
        for i in range(4):
            nx, ny = curr_x + dx[i], curr_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if maps[nx][ny] != 0:
                    maps[nx][ny] = maps[curr_x][curr_y] + 1
                    visited[nx][ny] = True
                    q.append((nx,ny))
    
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1


def solution(maps): 
    answer = bfs(maps)
    return answer
