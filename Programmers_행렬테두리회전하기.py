def show(graph):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            print(graph[i][j], end ='  ')
        print()
    print()
        
def solution(rows, columns, queries):
    answer = []
    
    # 그래프 초기화하기
    graph = [[0] * (rows+2) for _ in range(columns+2)]
    start = 1
    for i in range(1,columns+1):
        for j in range(1,rows+1):
            graph[i][j] = start
            start += 1
    rotated_numbers = []
    # 쿼리문의 요청대로 회전 수행
    for query in queries:
        x1,y1,x2,y2 = query
        while x2 -x1 > 1 and y2 - y1 > 1:
            # 회전 가능한 영역을 시계방향으로 회전
            temp1 = graph[x1][y2]
            for i in range(y2,y1,-1):
                graph[x1][i] = graph[x1][i-1]
            
            temp2 = graph[x2][y2]
            for i in range(x2,x1+1,-1):
                graph[i][y2] = graph[i-1][y2]
            graph[x1][y2] = temp1
        
            temp3 = graph[x2][y1]    
            for i in range(y1,y2):
                graph[x2][i] = graph[x2][i+1]
            graph[x2][y2] = temp2
        
            temp4 = graph[x2][y1]
            graph[x1][y1] = temp3    
            for i in range(x1,x2):
                graph[i][y1] = graph[i+1][y1]
            graph[x1][y1] = temp3
            
            x1 += 1
            y1 += 1
            x2 -= 1
            y2 -= 1
            
            show(graph)
    
    return answer

rows, columns = 6, 6
queries = 	[[2,2,5,4],[3,3,6,6],[5,1,6,3]]
solution(rows,columns,queries)