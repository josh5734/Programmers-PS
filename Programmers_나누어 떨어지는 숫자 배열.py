def solution(arr, divisor):
    array = sorted(arr)
    answer = []
    for i in array:
        if i % divisor == 0:
            answer += [i]
    if answer == []:
        answer = [-1]

    return answer