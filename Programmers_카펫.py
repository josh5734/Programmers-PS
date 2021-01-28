def solution(brown, yellow):
    answer = []

    # 세로의 길이는 무조건 1이상이어야 하므로 가로의 길이는 (brown-2)//2 가 최대임
    for w in range(1, (brown-2)//2+1):
        # 세로의 길이는 가로의 길이보다 작거나 같다는 조건
        for h in range(1, w+1):
            if (w-2) * (h-2) == yellow and w*h == yellow + brown:
                answer = [w, h]
                return answer
