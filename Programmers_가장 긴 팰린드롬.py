def isPalidrome(str):
    # 왼쪽끝, 오른쪽에서부터 좁혀오면서 비교하기
    left, right = 0, len(str)-1
    while(left < right):
        if str[left] != str[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

def solution(s):
    answer = 0
    # 가장 긴 문자열 길이부터 탐색하면서 팰린드롬이면 종료
    for length in range(len(s), 0, -1):
        for i in range(0, len(s) - length + 1):
            if isPalidrome(s[i:i+length]):
                return length

s = "a"
print(solution(s))