from collections import deque


def solution(priorities, location):
    printer = deque()
    for idx, priority in enumerate(priorities):
        printer.append((idx, priority))

    priorities.sort(reverse=True)  # 우선순위가 높은 순서대로 정렬
    max_idx = 0

    count = 0
    while True:
        idx, p = printer.popleft()
        if p == priorities[max_idx]:  # p가 우선순위가 가장 높다면 제거
            count += 1
            max_idx += 1  # 기존 priorities 배열에서 idx를 +1 해서 다음 최고 우선순위값 서치
            if idx == location:
                return count
        else:
            printer.append((idx, p))


if __name__ == "__main__":
    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    print(solution(priorities, location))
