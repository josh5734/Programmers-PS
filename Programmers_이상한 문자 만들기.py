def solution(s):
    space = []
    for j in range(len(s)):
        if s[j] == ' ':
            space.append(j)

    new_list = s.split()
    answer = []
    for i in new_list:
        s = ''
        for j in range(len(i)):
            if j % 2 == 0:
                s += i[j].upper()
            else:
                s += i[j].lower()
        answer.append(s)
    k = ''.join(answer)

    list = []
    for a in k:
        list.append(a)
    for s in space:
        list.insert(s, ' ')
    return ''.join(list)