def solution(numbers, target):
    answer_list = [0]
    for i in numbers:
        sum_list = []
        for j in answer_list:
            sum_list += [j + i]
            sum_list += [j - i]
        answer_list = sum_list

    answer = answer_list.count(target)
    return answer