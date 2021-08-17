from collections import Counter as C

def solution(clothes):
    answer = 1
    cloth_li = []
    for i in clothes:
        cloth_li.append(i[1])
    cloth_num = C(cloth_li)
    for type in cloth_num.keys():
        answer *= cloth_num[type]+1
    answer -= 1
    return answer