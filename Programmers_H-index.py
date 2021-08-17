def solution(citations):
    ans = 0
    citations.sort(reverse = True)
    for i in range(len(citations)):
        if i < citations[i]:
            ans = i+1
    return ans