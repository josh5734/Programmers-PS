import math


def solution(progresses, speeds):
    deploys = []
    while progresses:
        days_needed = math.ceil((100 - progresses[0]) / speeds[0])

        # 배포할 기능의 수
        count = 0
        for i in range(len(progresses)):
            progresses[i] += days_needed * speeds[i]

        # 기능이 맨 앞에 있고, 완성되어 있다면 목록에서 pop
        while progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            if len(progresses) == 0:
                break
        deploys.append(count)

    return deploys


if __name__ == "__main__":
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]

    print(solution(progresses, speeds))
