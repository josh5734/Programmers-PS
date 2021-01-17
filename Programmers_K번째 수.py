def solution(array, commands):
    answer =[]
    li = []
    for i in commands:
        li = array[i[0]-1:i[1]]
        li.sort()
        print(li)
        answer.append(li[i[2]-1])
    return answer