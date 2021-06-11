from collections import defaultdict

def solution(info, query):
    answer = []
    
    # query문 각각에 대해 info 분석
    for i in range(len(query)):
        # query문 parsing
        query[i] = query[i].replace("and","").split(" ")
        
        count = 0
        for j in range(len(info)):
            satisfied = True    # 조건을 만족하는가
            for k in range(4):  # 점수를 제외한 4가지 항목 체크
                if query[i][k] == '-':
                    continue

                if query[i][k] != info[j].split()[k]:
                    satisfied = False
                    
            if query[i][4] == '-': # 점수 체크
                continue
            else:
                if int(query[i][4]) > int(info[j].split()[4]):
                    satisfied = False

            if satisfied:
                count += 1
        answer.append(count)
        
    return answer
