def min_common_mul(a, b):
    x = min(a,b)
    flag = True
    while flag:
        if x % a == 0 and x % b == 0:
            flag = False
            return x
        else:
            x += 1
def solution(arr):
    answer = arr[0]
    for i in arr:
        answer = min_common_mul(answer,i)
    return answer