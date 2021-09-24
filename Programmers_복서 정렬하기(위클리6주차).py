from collections import defaultdict
def solution(weights, head2head):
    info = defaultdict(list)
    length = len(weights)
    
    for i in range(length):
        # 자신의 몸무게
        myWeight = weights[i]
        fight = head2head[i]
        wins, overWeightWins, totalGames = 0, 0, 0
        for j in range(length):
            # 상대방의 몸무게
            yourWeight = weights[j]
            if i == j or fight[j] == "N": continue
            if fight[j] == "W":
                wins += 1
                if myWeight < yourWeight:
                    overWeightWins += 1
            totalGames += 1
            
        info[i+1].append(wins/totalGames) if totalGames > 0 else info[i+1].append(0)
        info[i+1].append(overWeightWins)
        info[i+1].append(myWeight)
        info[i+1].append(i+1)
    sortedList = sorted(info.values(), key = lambda x : (-x[0], -x[1], -x[2], x[3]))
    answer = [sortedList[idx][3] for idx in range(length)]
    return answer
            
