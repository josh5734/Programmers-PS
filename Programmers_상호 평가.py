def setGrade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'
        
def solution(scores):
    answer = ''
    n = len(scores)

    for i in range(n):
        myScores = [] # 자신이 받은 점수
        for j in range(n):
            myScores.append(scores[j][i])
        
        # 자신의 점수가 유일한 최대 혹은 최소라면 전체 점수에서 제외
        total,count = sum(myScores), n
        myScore = myScores[i]
        if (myScore == max(myScores) or myScore == min(myScores)) and myScores.count(myScore) == 1:
            total -= myScore
            count -= 1
        answer += setGrade(total / count)
    return answer

