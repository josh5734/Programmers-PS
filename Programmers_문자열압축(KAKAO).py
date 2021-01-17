import re


def solution(s):
    if len(s) <= 2:
        return (len(s))
    resultcount = []
    for i in range(1, len(s) // 2 + 1):
        relist = re.sub('(\w{%i})' % i, '\g<1> ', s).split()
        count = 1
        result = []
        for j in range(len(relist)):
            if j < len(relist) - 1 and relist[j] == relist[j + 1]:
                count += 1
            else:
                if count == 1:
                    result.append(relist[j])
                else:
                    result.append(str(count) + relist[j])
                    count = 1

        resultcount.append(len(''.join(result)))
    return min(resultcount)