from collections import defaultdict
def solution(gems):
    answer = []
    # 전체 보석이 몇 개 있는지 확인
    gemsDict = defaultdict(int)
    totalGems = len(set(gems))
    length = len(gems)
    maxLength = 1000000

    left, right = 0, 0
    gemsDict[gems[left]] = 1
    count = 1

    # 투포인터를 구간 끝까지 탐색
    while left < length and right < length:

        # 모든 보석을 담았으면 왼쪽 포인터를 이동시켜본다.
        if count == totalGems:
            # 구간 길이가 최소이고, 인덱스가 작은 값을 기록
            # 왼쪽에서 오른쪽으로 포인터가 이동하므로 자동으로 인덱스는 작은 것이 최종적으로 기록된다.
            if right - left < maxLength:
                maxLength = right - left
                answer = [left + 1, right + 1]
            
            gemsDict[gems[left]] -= 1
            if gemsDict[gems[left]] == 0:
                count -= 1
            left += 1

        # 보석이 부족하면 오른쪽으로 구간을 확장해본다.
        else:
            right += 1
            if right < length:
                gemsDict[gems[right]] += 1
                if gemsDict[gems[right]] == 1:
                    count += 1

            # 구간에 끝까지 갔으면 더 이상 추가할 보석이 없음
            else:
                break
    return answer

        
# print(solution(gems=["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# print(solution(gems=["A","B","B","C","A"]))
# print(solution(gems=["XYZ", "XYZ", "XYZ"]))
# print(solution(gems=["a"]))
# print(solution(gems=["a","a","a","b","b"]))
print(solution(gems=["A","B","B","B","B","B","B","C","B","A"]))

'''
def solution(gems): 
    answer = []
    # 전체 보석이 몇 개 있는지 확인
    totalGems = len(set(gems))

    length = len(gems)
    maxLength = 1000000
    left = 0
    for left in range(length):
        currGems = set()
        right = left
        exist = False
        while right < length:
            currGems.add(gems[right])
            if len(currGems) == totalGems:
                if right - left + 1 < maxLength:
                    maxLength = right - left + 1
                    answer = [left + 1, right + 1]
                exist = True
                break
            else:
                right += 1
        if not exist:
            break
        currGems.remove(gems[left])
    return answer
'''