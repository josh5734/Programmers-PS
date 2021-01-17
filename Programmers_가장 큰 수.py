def solution(numbers):

    answer =''
    ans = []
    order_li = []
    ans_li = []
    for i in numbers:
        i = str(i)
        i *= 4
        order_li.append(i)
    for num in sorted(order_li,reverse=True):
        ans_li.append(order_li.index(num))

    for i in ans_li:
        answer += str(numbers[i])
    if answer[0] == '0':
        return '0'
    return answer