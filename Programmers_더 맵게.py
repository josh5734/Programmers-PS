import heapq


def solution(scovile, K):
    count = 0
    foods = []
    # 최소힙에 scovile 지수 정보 입력
    for f in scovile:
        heapq.heappush(foods, f)

    while True:
        firstMin = heapq.heappop(foods)
        secondMin = heapq.heappop(foods)
        heapq.heappush(foods, firstMin + (secondMin * 2))
        count += 1
        if foods[0] >= K:
            return count
        if len(foods) == 1 and foods[0] < K:
            return -1


if __name__ == "__main__":
    solution(scovile, K)
