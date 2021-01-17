from itertools import permutations as P


def check_prime_num(n):
    if n != 1:
        for f in range(2, n):
            if n % f == 0:
                return False
    else:
        return False

    return True


def solution(numbers):
    answer = 0
    distinct_li = []
    num = len(numbers)
    for i in range(num):
        distinct_li.append(numbers[i])
    for i in range(1, num + 1):
        temp_li = list(set(map(''.join, P(distinct_li, i))))

        for j in temp_li:
            if check_prime_num(int(j)) == True and j[0] != '0':
                answer += 1
    return answer


solution('011')