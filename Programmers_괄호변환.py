def isRightBucket(p): # 올바른 괄호 문자열인지 확인 - 스택 이용
    if len(p) == 0:
        return True
    stack = []
    for b in p:
        if len(stack) == 0:
            stack.append(b)
        elif b == '(':
            stack.append(b)
        elif b == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(b)
    return len(stack) == 0


# 균형잡힌 괄호 문자열인지 확인하는 함수
def isBalancedBucket(p):
    if len(p) == 0:
        return True
    left, right = 0, 0
    for b in p:
        if b == '(':
            left += 1
        elif b == ')':
            right += 1

        if left == right:
            return True
    return False

def divideUV(p): # 균형맞는 괄호 문자열 두 개로 쪼개기
    length = len(p)
    u, v = "", ""
    for i in range(1, length+1): # range(1, length+1) 까지 해야 아래 isBalancedBucket에 매개변수로 넣을때 맞음!
        if isBalancedBucket(p[:i]):
            u, v = p[:i], p[i:]
            break
    return u, v


def makeU(u):
    u = list(u[1:-1])
    for i in range(len(u)):
        u[i] = ')' if u[i] == '(' else '('
    return "".join(u)


def solution(p):
    if isRightBucket(p):
        return p  # 이미 올바른 괄호 문자열이면 리턴
    u, v = divideUV(p)  # 두 균형잡힌 문자열 u, v로 바꿈
#    print(u, v)

    # u가 올바른 괄호 문자열일 때
    if isRightBucket(u):
        return u + solution(v)
    # u가 올바른 괄호 문자열이 아닐 때
    if not isRightBucket(u):
        temp = "(" + solution(v) + ")" + makeU(u)
        return temp


if __name__ == "__main__":
    p = ""
    p1 = "(()())()"
    p2 = ")("
    p3 = "()))((()"
    # print(solution(p1))
    # print(solution(p2))
    print(solution(p2))
