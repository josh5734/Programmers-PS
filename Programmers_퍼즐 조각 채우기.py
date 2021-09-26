def show(graph):
    n = len(graph)
    for i in range(n):
        for j in range(n):
            print(graph[i][j], end = ' ')
        print()

def rotate(table):
    n = len(table)
    new_table = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_table[i][j] = table[j][n-i-1]
    return new_table

def dfs(graph,visited, i, j,s):
    size = len(graph)
    visited[i][j] = True
    stack, blocks = [[i,j]], [[i,j]]
    dx, dy = [1,-1, 0,0], [0,0,1,-1]
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < size and 0 <= ny < size and not visited[nx][ny] and graph[nx][ny] == s:
                visited[nx][ny] = True
                stack.append([nx,ny])
                blocks.append([nx,ny])
    return blocks


# 빈 공간을 (0,0) 기준으로 몰아넣기
def rearrange(shape):
    minX = min([x[1] for x in shape])
    minY = min([x[0] for x in shape])
    shape = [(s[0]-minY, s[1]-minX) for s in shape]
    return sorted(shape) # 블록이 여러 칸으로 이루어진 경우 같은 모양에서 같은 결과를 위해 정렬해서 반환


def solution(game_board, table):
    answer = 0
    size = len(game_board)
    
    # game_board에 존재하는 빈 공간을 dfs로 탐색
    empty_space = []
    table_block = []

    for i in range(4):
        board = rotate(game_board)
        visited = [[False] * size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                if game_board[i][j] == 0 and not visited[i][j]:
                    temp = rearrange(dfs(game_board,visited, i, j, 0))
                    if temp not in empty_space:
                        empty_space.append(temp)
                    
    # 테이블을 회전해보기
    for i in range(4):
        table = rotate(table)
        # 회전한 테이블에 있는 블록 조각들의 정보
        visited = [[False] * size for _ in range(size)]
        for j in range(size):
            for k in range(size):
                if table[j][k] == 1 and not visited[j][k]:
                    table_block.append(dfs(table, visited, j, k, 1))
        
    # 게임 보드의 공간에 들어맞는 블록 조각이 있는지 확인해보기
    for block in table_block:
        r_block = rearrange(block)
        for space in empty_space:
            if space == r_block:
                print(space)
                answer += len(space)
                empty_space.remove(space)
                for b in block:
                    table[b[0]][b[1]] = 0
    return answer

game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
print(solution(game_board, table))


x = [[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
y = [[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]]
#print(solution(x,y))