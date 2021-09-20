import heapq

def solution(n, start, end, roads, traps):
    pq = []
    heapq.heappush(pq, ((0, start, roads)))
    trapChk = [False] * (n+1)
    for t in traps:
        trapChk[t] = True

    while pq:
        currDistance, currPos, roadInfo = heapq.heappop(pq)
        if currPos == end:
            return currDistance

        # 현재 위치가 트랩
        if trapChk[currPos]:
            newRoadInfo = []
            for i in range(len(roadInfo)):
                # 현재 위치에서 나가거나 들어오는 방향을 전환 
                if roadInfo[i][0] == currPos or roadInfo[i][1] == currPos:
                    temp = [roadInfo[i][1], roadInfo[i][0], roadInfo[i][2]]
                    newRoadInfo.append(temp)
                else:
                    newRoadInfo.append(roadInfo[i])
            roadInfo = newRoadInfo

        # 현 위치에서 갈 수 있는 곳들을 방문
        for road in roadInfo:
            s, e, dist = road[0], road[1], road[2]
            if s == currPos:
                heapq.heappush(pq,(currDistance + dist, e, roadInfo))
                
n, start, end = 4, 1, 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]
print(solution(n, start, end, roads, traps))