from itertools import permutations as p
from math import sqrt


def check_prime_num(n):
    if n == 0 or n == 1:
        return False

    if n == 2:
        return True

    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False

    return True


def solution(numbers):
    answer = 0
    # 주어진 숫자 목록
    number_list = list(numbers)

    for i in range(1, len(number_list)+1):
        # i개의 숫자를 가지고 모든 경우의 수를 찾기
        temp_li = list(set(map(''.join, p(numbers, i))))

        # 각 경우에 대하여 소수인지 확인
        for j in temp_li:
            if check_prime_num(int(j)) == True and j[0] != '0':
                answer += 1
    return answer


print(solution('011'))
