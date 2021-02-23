def solution(w, h):
    if w == 1 or h == 1:
        return 0
    if w == h:
        return w*h - w
    answer = w*h-1
    # 가로, 세로중에 짧은 곳을 가로, 긴 곳을 세로로 고정
    w, h = min(w, h), max(w, h)

    # 한 행씩 내려갈때마다 격자가 x축방향으로 이동하는 길이
    dx = w / h
    for i in range(1, h):
        start, end = dx * i, dx * (i+1)
        # 끝부분이 모서리에 닿지 않고, 격자선이 한 변을 뚫고 지나갈 때는 두개가 날라감
        if end - int(end) != 0 and (int(end) - int(start) == 1):
            answer -= 2
        else:
            answer -= 1
    return answer


if __name__ == "__main__":
    w, h = 8, 12
    print(solution(w, h))
