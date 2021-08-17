######### 풀이 1 ###########
def solution(number, k):
    answer = []

    for num in number:
        if len(answer) == 0:
            answer.append(num)
        else:
            while len(answer) > 0 and answer[-1] < num and k > 0:
                answer.pop()
                k -= 1
            answer.append(num)
    if k > 0:
        answer = answer[:-k]
    return ''.join(answer)

######### 풀이 2 ###########


def solution(number, k):
    num = list(number)
    answer = [num[0]]
    cnt = 0

    for i in range(1, len(num)):
        if cnt == k:
            answer += num[i:]
            break

        answer.append(num[i])
        if(answer[-1] > answer[-2]):
            while(len(answer) != 1 and answer[-1] > answer[-2] and cnt < k):
                answer[-1], answer[-2] = answer[-2], answer[-1]
                answer.pop()
                cnt += 1

    return ''.join(answer[:len(num)-k])
