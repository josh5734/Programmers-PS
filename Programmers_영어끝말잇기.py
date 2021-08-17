def solution(n, words):
    answer = [0,0]
    
    pre_used = [words[0]] # 이미 사용한 단어
    lastChar = words[0][-1] # 마지막 단어 알파벳
    
    for i in range(1, len(words)):
        if words[i].startswith(lastChar) and words[i] not in pre_used:
            lastChar = words[i][-1]
            pre_used.append(words[i])
            
        else:
            # i번째 단어에서 탈락
            number = (i+1) % n
            if number == 0: number = n
            turn = (i+1) / n
            if int(turn) != turn: turn = int(turn) + 1
            answer[0], answer[1] = number, turn
            break   # 게임 종료
    return answer
