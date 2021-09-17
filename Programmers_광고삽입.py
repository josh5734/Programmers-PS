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
    for log in logs:
        start, end = log[0], log[1]
        onWatching[start] += 1
        onWatching[end] -= 1


    for i in range(1, play_time+1):
        onWatching[i] += onWatching[i-1]

    t = 0
    total = 0 

    # t = 0 일때 누적 시청량 초기화
    for i in range(adv_time+1):
        total += onWatching[i]
    totalMax = total
    answer = [(0,0)]

    # 모든 가능한 광고 시작 시간에 대해 슬라이딩 윈도우 
    while t < play_time - adv_time:
        total += onWatching[t + adv_time] - onWatching[t]
        if totalMax < total:
            totalMax = total
            answer.append((total,t+1))
        t += 1

    answer = sorted(answer, key = lambda x : (x[0], -x[1]))
    return parseIntoHour(answer[-1][1])


play_time = "99:59:59"
adv_time = "25:00:00"
logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
# print(solution(play_time,adv_time,logs))

play_time2 = "02:03:55"
adv_time2 = "00:14:15"
logs2 = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
# print(solution(play_time2,adv_time2,logs2))

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


def solution(play_time, adv_time, logs):
   answer = ''
   adv_time = time_converter(adv_time)
   play_time = time_converter(play_time)
   watch_logs = [0 for _ in range(play_time)]
   print(play_time, adv_time, len(watch_logs))
   # 여기서 시간이 오래걸림...
   for log in logs:
       s = log.split("-")
       start, end = time_converter(s[0]), time_converter(s[1])
       while start < end:
           watch_logs[start] += 1
           start += 1

   temp = sum(watch_logs[:adv_time])
   max_time = temp
   answer = 0
   s, e = 0, adv_time
   while e < play_time:
       if temp - watch_logs[s] + watch_logs[e] > max_time:
           max_time = temp - watch_logs[s] + watch_logs[e]
           answer = s + 1
       temp = temp - watch_logs[s] + watch_logs[e]
       s += 1
       e += 1

   hh, mm, ss = answer // 3600, (answer % 3600) // 60, answer % 60

   return f"{str(hh).zfill(2)}:{str(mm).zfill(2)}:{str(ss).zfill(2)}"


def time_converter(s):
   time = list(map(int, s.split(":")))
   return 3600 * time[0] + 60 * time[1] + time[2]


p = "50:00:00"
a = "50:00:00"
l = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
print(solution(p, a, l))
