from collections import deque


def solution(numbers, target):
    q = deque()
    # 처음에 0을 넣고 시작
    q.append(0)
    # 주어진 numbers를 앞에서부터 순회
    while numbers:
        # 현재 단계의 값들에 대해 +, -를 해서 나올 수 있는 경우를 temp에 저장
        temp = []
        while q:
            now = q.popleft()
            temp.append(now + numbers[0])
            temp.append(now - numbers[0])
        numbers.pop(0)
        # temp를 q에 저장
        q.extend(temp)

    # 결과적으로 q에는 numbers를 서치하면서 +, -한 최종 결과가 저장됌
    return q.count(target)


if __name__ == "__main__":
    numbers = [1, 1, 1, 1, 1]
    target = 3
    answer = solution(numbers, target)
    print(answer)
