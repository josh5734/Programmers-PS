def solution(answers):
    pattern_1 = [1,2,3,4,5]
    pattern_2 = [2,1,2,3,2,4,2,5]
    pattern_3 = [3,3,1,1,2,2,4,4,5,5]
    scores = [0, 0, 0]
    answer = []
    for idx in range(0,len(answers)):
        if pattern_1[idx % 5] == answers[idx]:
            scores[0] += 1
        if pattern_2[idx % 8] == answers[idx]:
            scores[1] += 1
        if pattern_3[idx % 10] == answers[idx]:
            scores[2] += 1
    max_score = max(scores)
    for i in range(3):
        if scores[i] == max_score:
            answer.append(i+1)
    return answer