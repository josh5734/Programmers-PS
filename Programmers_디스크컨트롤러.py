import heapq
def solution(jobs):
    totalTime, currentTime = 0, 0
    n = len(jobs)
    pq = []

    # 작업을 들어온 순, 소요시간이 적은 순서대로 정렬
    jobs.sort(key = lambda x : (x[0], x[1]))

    while jobs:
        print(currentTime, jobs)
        # 만약 현재 시간에 작업이 없다면 다음에 들어오는 녀석 바로 수행
        if currentTime <= jobs[0][0]:
            arriveTime, requestTime = jobs.pop(0)
            currentTime = arriveTime + requestTime
            totalTime += requestTime
        
        # 현재 시간에 이미 들어온 작업이 있다면 소요 시간이 적은 녀석을 먼저 수행
        else:
            temp = []
            for arriveTime, requestTime in jobs:
                if arriveTime <= currentTime:
                    temp.append([arriveTime,requestTime])
            temp.sort(key = lambda x : -x[1])
            nextJob = temp.pop()
            arriveTime, requestTime = nextJob[0], nextJob[1]
            currentTime += requestTime
            totalTime += currentTime - arriveTime

            jobs.remove(nextJob)    # 수행한 작업을 빼주기
            jobs.sort(key = lambda x : (x[0], x[1]))
    return int(totalTime / n)
                
            

if __name__ == "__main__":
    jobs = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
    jobs2 = [[0, 3], [1, 9], [2, 6]]
    time = solution(jobs)
    print(time)