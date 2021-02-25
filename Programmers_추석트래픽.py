
def TimeParserToSec(request):
    # "2016-09-15 hh:mm:ss.sss"
    hour, minute, sec = request[11:13], request[14:16], request[17:23]
    return float(hour) * 60 * 60 + float(minute) * 60 + float(sec)


def solution(lines):
    n = len(lines)
    if n == 1:
        return 1
    start_end_of_request = []
    # 요청의 시작, 종료 시간을 파싱하여 리스트에 담는다.
    for request in lines:
        request = request[:-1]  # 맨 뒤에 s 제거
        # 각 요청의 시작, 종료 시간
        end_time = TimeParserToSec(request)
        requestTime = float(request[24:]) - 0.001
        start_time = float(format((end_time - requestTime), ".3f"))
        start_end_of_request.append(
            (start_time * 1000, end_time * 1000))  # 초 단위로 바꾸기

    answer = 0
    # 요청이 받아지는 순서대로 정렬\
    start_end_of_request.sort()
    for t in start_end_of_request:
        for tt in t:
            tt = int(tt)
            count = 0
            for i in range(n):
                start, end = start_end_of_request[i][0], start_end_of_request[i][1]
                if start <= tt <= end:
                    count += 1
            if answer <= count:
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

    print(solution(lines1))
    print(solution(lines2))
    print(solution(lines3))
