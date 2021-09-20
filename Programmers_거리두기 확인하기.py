def checkBounds(x, y):
   return 0 <= x < 5 and 0 <= y < 5
 
def solution(places):
   answer = []
  
   # 각 지점에 대해 오른쪽, 아래, 대각선 왼쪽아래, 대각선 오른쪽 아래만 관찰
   dx, dy = [0,1,1,1],[1,0,-1,1]
   for room in places:
       flag = True # 거리두기가 지켜졌는지 확인하는 플래그 변수
       for i in range(5):
           for j in range(5):
               if room[i][j] != "P": continue
   
               for d in range(4):
                   ni, nj = i + dx[d], j + dy[d]
                   if not checkBounds(ni,nj): continue
 
                   # 바로 오른쪽이나 아래에 사람이 있으면 False
                   if d == 0 or d == 1:
                       if room[ni][nj] == "P":
                           flag = False
                           break
                       else:
                           # 1만큼 더 간 지점에 사람이 있고 가운데는 빈 테이블이면 False
                           nni, nnj = ni + dx[d], nj + dy[d]
                           if not checkBounds(nni,nnj):continue
                       
                           if room[ni][nj] + room[nni][nnj] == "OP":
                               flag = False
                               break
 
                       # 대각선에 왼쪽 아래 위치하고 부근에 파티션이 한 곳이라도 없으면 False
                       if d == 2 and room[ni][nj] == "P":
                           if room[i][j-1] != "X" or room[i+1][j] != "X":
                               flag = False
                               break
                       # 대각선에 오른쪽 아래 위치하고 부근에 파티션이 한 곳이라도 없으면 False
                       if d == 3 and room[ni][nj] == "P":
                           if room[i][j+1] != "X" or room[i+1][j] != "X":
                               flag = False
                               break
       answer.append(1 if flag else 0)
   return answer
