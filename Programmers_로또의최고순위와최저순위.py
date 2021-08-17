def solution(lottos, win_nums):
    answer = []
    correct = 0
    
    for l in lottos:
        for w in win_nums:
            if l == w:
                correct += 1
    zeros = lottos.count(0)
    # 최고순위
    answer.append(min(6,7 - (correct + zeros)))
 
    # 최저순위 - zero가 다 틀렸음을 가정
    if correct <= 1:
        answer.append(6)
    else:
        answer.append(7-correct)
    
    return answer