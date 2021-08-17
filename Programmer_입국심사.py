def binarySearch(start, end, times, n):
    answer = 0

    search = True
    while start <= end:
        mid = int((start + end) / 2)

        count = 0

        for time in times:
            count += int((mid/time))
        if count < n:
            start = mid + 1
        elif count >= n:
            end = mid - 1
            answer = mid
    return answer


def solution(n, times):
    times.sort()
    min_time = times[0]
    max_time = times[-1] * n
    answer = binarySearch(min_time, max_time, times, n)
    return answer
