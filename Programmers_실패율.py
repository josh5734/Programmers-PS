def solution(N, stages):
    onStagePlayers = [0] * (N+2)
    stageNotClearPlayers = [0] * (N+2)

    for stage in stages:
        for i in range(1, stage+1):
            onStagePlayers[i] += 1
    for stage in stages:     
        stageNotClearPlayers[stage] += 1
    result = []
    stageNumber = 1
    # 0번째, N+1 번째 스테이지 제외
    for i, j in zip(onStagePlayers[1:-1], stageNotClearPlayers[1:-1]):
        if i > 0:
            result.append([stageNumber, j/i])
        else:
            result.append([stageNumber, 0])
        stageNumber += 1
    result = sorted(result, key=lambda x: -x[1])  # 실패율이 높은 순서대로 정렬
    result = [x for x, y in result]  # 스테이지 번호만 추출
    return result


if __name__ == "__main__":
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]
    print(solution(N, stages))
