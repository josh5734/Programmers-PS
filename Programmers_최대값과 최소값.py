def solution(s):
    new_list = list((map(int,s.split(' '))))
    min_number = min(new_list)
    max_number = max(new_list)
    answer = ''
    answer += str(min_number)
    answer += ' '
    answer += str(max_number)
    return answer