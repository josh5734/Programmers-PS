def solution(n):
    a = n ** 0.5
    if int(a)-a == int(0):
        answer = (a+1)**2
    else:
        answer = -1
    return answer
    print(answer)