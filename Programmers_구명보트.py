def solution(people, limit):
    # 제일 무게 많이 나가는 사람과 제일 가벼운 사람이 같이 탈 수 있는지
    people.sort(reverse=True)
    boat = 0  # 필요한 보트 수
    count = 0  # 태워 보낸 사람 수
    first, last = 0, len(people)-1
    while count < len(people):
        if people[first] + people[last] <= limit:  # 두 명 태워 보내기
            first += 1  # 제일 무거운 사람 idx 증가
            last -= 1  # 제일 가벼운 사람 idx 감소
            count += 2  # 2명 추가
        else:  # 제일 무거운 사람 한 명만 태워 보내기
            first += 1  # 제일 무거운 사람의 idx 증가
            count += 1  # 1명 추가
        boat += 1
    return boat


if __name__ == "__main__":
    people = [1, 1, 1, 1, 1, 1]
    limit = 2
    answer = solution(people, limit)
    print(answer)
