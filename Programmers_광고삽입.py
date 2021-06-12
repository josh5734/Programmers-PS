# 초 단위로 parsing
def parseIntoSec(time):
    hour, min, sec = time.split(":")
    sec = 60 * 60 * int(hour) + 60 * int(min) + int(sec)
    return sec

def parseIntoHour(time):
    hour = time // 3600
    time -= 3600 * hour
    min = time // 60
    time -= 60 * min
    return str(hour).zfill(2) + ":" + str(min).zfill(2) + ":" + str(time).zfill(2)


def solution(play_time, adv_time, logs):
    # 초 단위로 주어진 시간들을 parsing하기
    play_time = parseIntoSec(play_time)
    adv_time = parseIntoSec(adv_time)
    for i in range(len(logs)):
        start, end = logs[i].split('-')
        start, end = parseIntoSec(start), parseIntoSec(end)
        logs[i] = (start,end)

    # 광고 시간과 전체 시간이 같은 경우    
    if play_time == adv_time:
        return "00:00:00"

    # play_time 동안 접속하고 있는 시청자 수
    onWatching = [0] * (play_time + 2)
    
    # 모든 시청 기록에 대해서 시작, 종료 시점을 기록
    enter, out = [], []
    for log in logs:
        start, end = log[0], log[1]
        onWatching[start] += 1
        onWatching[end+1] -= 1  # 나가는 시점까지는 영상 시청
    # t = 0 일때 누적 시청량
    t = 0
    total = 0
    net_change = 0  # 각 시점에서 들어오고 나가는 총 변화량
    for i in range(t+adv_time+1):
        net_change += onWatching[i]
        total += net_change
    totalMax = total
    answer = [(0,0)]

    while t < play_time - adv_time:
        t += 1
        net_change += onWatching[t + adv_time] - onWatching[t-1]
        total += net_change
        if totalMax <= total:
            totalMax = total
            answer.append((total,t))

    answer = sorted(answer, key = lambda x : (x[0], -x[1]))
    return parseIntoHour(answer[-1][1])

play_time = "99:59:59"
adv_time = "25:00:00"
logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
print(solution(play_time,adv_time,logs))

play_time2 = "02:03:55"
adv_time2 = "00:14:15"
logs2 = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution(play_time2,adv_time2,logs2))

p = "10:00:00"
a = "01:00:00"
l = ["01:00:00-02:00:00","01:00:00-02:00:00","01:00:00-02:00:00"]
print(solution(p,a,l))


'''
def solution(play_time, adv_time, logs):
    answer = ''
    # 초 단위로 주어진 시간들을 parsing하기
    play_time = parseIntoSec(play_time)
    adv_time = parseIntoSec(adv_time)
    for i in range(len(logs)):
        start, end = logs[i].split('-')
        start, end = parseIntoSec(start), parseIntoSec(end)
        logs[i] = (start,end)

    # 광고 시간과 전체 시간이 같은 경우    
    if play_time == adv_time:
        return "00:00:00"

    # 그 외의 경우에는 누적 시간이 최대가 되는 지점을 조사
    # 후보는 각 영상의 시청이 시작되는 지점
    candidates = []
    logs.sort()
    for log in logs:
        startTime = log[0]
        endTime = startTime + adv_time

        watchingTime = 0
        for other_log in logs:
            if other_log[1] <= startTime:
                continue
            if other_log[0] >= endTime:
                break
            watchingTime += min(other_log[1], endTime) - max(other_log[0], startTime)
        candidates.append((watchingTime, startTime))

    # 누적 시간이 가장 길고, 시작 시간이 가장 빠른 결과 출력        
    candidates = sorted(candidates, key = lambda x : (x[0],-x[1]))

    # 최초 영상 시청 시간보다 광고를 더 빨리 싣을 수 있는 경우?

    print(candidates[-1])
    return parseIntoHour(candidates[-1][1])
'''
