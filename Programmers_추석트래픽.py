
def TimeParserToSec(request):
    # "2016-09-15 hh:mm:ss.sss"
    time = request.split(" ")[1].split(":")
    hour, minute, sec = time[0], time[1], time[2]
    return (int(hour)*60*60 + int(minute)*60 + float(sec))*1000


def requestTimeParser(request):
    request_time = float(request.split(" ")[2].replace('s', "")) * 1000
    return request_time


def solution(lines):
    n = len(lines)
    if n == 1:
        return 1

    start_end_of_request = []
    # 요청의 시작, 종료 시간을 파싱하여 리스트에 담는다.

    for request in lines:
        # 각 요청의 시작, 종료 시간 파싱
        end_time = TimeParserToSec(request)
        requestTime = requestTimeParser(request)
        start_time = end_time - requestTime + 1
        start_end_of_request.append((start_time, end_time))

    answer = 1

    for t in start_end_of_request:
        for i in range(2):
            pivot = t[i]  # 각 요청의 시작, 종료 시간을 기점으로 검사 시작
            count = 0
            start, end = pivot, pivot + 1000
            for tt in start_end_of_request:
                if tt[1] >= start and tt[0] < end:  # 해당 요청의 시작과 끝이 pivot 기준 1000ms 안에 있다면 성공
                    count += 1
            if count >= answer:
                answer = count
    return answer


if __name__ == "__main__":

    lines1 = [
        "2016-09-15 01:00:04.001 2.0s",
        "2016-09-15 01:00:07.000 2s"
    ]

    lines2 = [
        "2016-09-15 01:00:04.002 2.0s",
        "2016-09-15 01:00:07.000 2s"
    ]
    lines3 = [
        "2016-09-15 20:59:57.421 0.351s",
        "2016-09-15 20:59:58.233 1.181s",
        "2016-09-15 20:59:58.299 0.8s",
        "2016-09-15 20:59:58.688 1.041s",
        "2016-09-15 20:59:59.591 1.412s",
        "2016-09-15 21:00:00.464 1.466s",
        "2016-09-15 21:00:00.741 1.581s",
        "2016-09-15 21:00:00.748 2.31s",
        "2016-09-15 21:00:00.966 0.381s",
        "2016-09-15 21:00:02.066 2.62s"
    ]

    # print(solution(lines1))
    # print(solution(lines2))
    print(solution(lines3))
