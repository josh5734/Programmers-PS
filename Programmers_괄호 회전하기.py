# 올바른 괄호 문자열인지 확인하는 함수
def isValidBusket(str):
    stack = []

    for s in str:
        if len(stack) == 0:
            stack.append(s)
        else:
            # 스택 마지막 원소가 여는 괄호이면서 현재 문자는 닫는 괄호
            if stack[-1] in bucketDict and s not in bucketDict:       
                # 두 괄호가 매치되지 않으면 False  
                if s != bucketDict[stack[-1]]:  
                    return False
                # 두 괄호가 매치되면 마지막 원소를 pop
                else:
                    stack.pop()
            # 스택 마지막과 현재 문자가 둘 다 여는 괄호면 append
            elif stack[-1] in bucketDict and s in bucketDict:
                stack.append(s)
            # 스택 마지막이 닫는 괄호면 올바른 괄호 아님
            else:
                return False
    return True if len(stack) == 0 else False

def solution(s):
    answer = 0
    # 왼쪽으로 회전시켜보기
    for x in range(len(s)):
        rotated = s[x:] + s[:x]
        if isValidBusket(rotated):
            answer += 1

    return answer

# 괄호 대응 정보를 가진 딕셔너리
bucketDict = {'(': ')', '{':'}', '[':']'}