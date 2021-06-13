from itertools import combinations as C

def isPrime(num):
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    
    # 주어진 nums에 대해 3개의 숫자를 선택하는 경우를 모두 탐색
    comb_nums = list(C(nums, 3))
    
    for c in comb_nums:
        if isPrime(sum(c)):
            answer += 1
    
    return answer


if __name__ == "__main__":
    nums = [1,2,3,4,5,6]
    print(solution(nums))