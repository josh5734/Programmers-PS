import re


def solution(files):
    temp = [re.split(r'([0-9]+)', s) for s in files]
    print(temp)

    sort = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])))
    print(sort)

    return ["".join(s) for s in sort]