def tupleStringToList(s):
    tuple_list = []
    for i in range(1, len(s)-1):
        if s[i] == "{":
            # 하나의 리스트가 생성되고, 숫자 초기화
            integer = ""
            tuple2list = []
        elif s[i] == ",":
            # 튜플 사이의 쉼표가 아닐 때 숫자 초기화하고 리스트에 추가
            if s[i-1] != "}":   
                tuple2list.append(int(integer))
                integer = ""
        elif s[i] == "}":
            # 하나의 리스트가 끝나면 해당 리스트를 전체 튜플 리스트에 추가
            tuple2list.append(int(integer))
            tuple_list.append(tuple2list)
        else:
            integer += s[i]

    return tuple_list


def solution(s):
    answer = []

    # 튜플을 리스트 형태로 바꾼다.
    tuple_list = tupleStringToList(s)
    tuple_list.sort(key = lambda x : len(x))

    for lst in tuple_list:
        for number in lst:
            if number not in answer:
                answer.append(number)
    return answer

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))