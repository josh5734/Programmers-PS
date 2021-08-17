def solution(a, b):
    i = 0
    if a <= b:
        for k in range(a,b+1):
            i += k
    else:
        for k in range(b, a+1):
            i += k
    return i