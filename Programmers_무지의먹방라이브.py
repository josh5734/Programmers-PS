from collections import deque


def solution(food_times, k):
    foods = []
    for idx, food_amount in enumerate(food_times):
        foods.append([food_amount, idx+1])

    foods.sort()  # 음식 양이 적은 순서대로 정렬 - 배열 길이에 영향을 주기 때문
    if sum(food_times) <= k:  # k가 전체 음식 양보다 크거나 같으면 -1
        return -1

    minFoodAmount = foods[0][0]
    length = len(foods)
    oneCycleTime = minFoodAmount * length  # oneCycleTime이 되면 음식이 하나 사라짐
    nextFoodIdx = 1  # 두번째에 있는 음식이 1초 후에 사라지므로 1로 두번째 음식을 가리키도록 초기화
    while oneCycleTime <= k:  # 더 이상 사라지는 음식이 없으면 loop 종료
        k -= oneCycleTime
        minFoodAmount = foods[nextFoodIdx][0] - foods[nextFoodIdx-1][0]
        length -= 1
        oneCycleTime = minFoodAmount * length
        nextFoodIdx += 1
    foods = foods[nextFoodIdx-1:]  # 지금까지 다 먹은 음식 제거
    foods = sorted(foods, key=lambda x: x[1])  # 다시 원래 인덱스순으로 정렬
    idx = k % len(foods)  # 남은 음식들 중에서 k번째 구하기
    return foods[idx][1]

# k가 매우 크면 O(N)의 시간복잡도에서 효율성 테스트 실패할 것
# 한 바퀴를 도는 시간이 달라지는 기점은 남은 양이 최소인 음식이라는 점을 생각해보자.
# 효율성 테스트 하나 성공 / 정확성 테스트 전부 성공


def solution3(food_times, k):
    foods = []
    for idx, food_amount in enumerate(food_times):
        foods.append([food_amount, idx+1])
    foods.sort(reverse=True)
    while len(foods) > 0:
        minFoodAmount = foods[-1][0]
        oneCycleLength = len(foods)
        cycle = k // (minFoodAmount * oneCycleLength)

        if cycle >= 1:
            k -= minFoodAmount * oneCycleLength
            rem = 0  # 아직 남아 있는 음식까지 슬라이싱하기 위한 변수
            for i in range(len(foods)-1, -1, -1):
                foods[i][0] -= minFoodAmount
                if foods[i][0] <= 0:
                    rem = i
            foods = foods[:rem]
        elif cycle == 0:  # 남은 시간동안 사라지는 음식이 없다면 그 안에 정답이 있음
            foods = sorted(foods, key=lambda x: x[1])  # 인덱스순으로 정렬
            idx = k % len(foods)
            return foods[idx][1]

    return -1

# 회전판과 상황을 생각해보면 queue 자료구조를 이용하는 것 같다.
# 아래 풀이는 직관적으로 떠오르지만 정확성 테스트는 다 맞고, 효율성 테스트 실패


def solution2(food_times, k):
    # 큐에 food_times를 넣고 시작
    q = deque()
    for idx, food in enumerate(food_times):
        q.append((idx+1, food))

    count = 0
    while count < k:  # k초에서 중단
        if not q:  # 아직 k초가 되지 않았는데 q가 비었으면 -1 return
            return -1
        food_idx, food_amount = q.popleft()
        if food_amount > 1:  # 이번 기회에 먹고 다음 기회에도 먹을 수 있다면 다시 큐에 삽입
            q.append((food_idx, food_amount-1))
        count += 1
    # 이제 먹어야 할 음식의 인덱스를 리턴
    if not q:
        return -1
    else:
        return q.popleft()[0]


if __name__ == "__main__":
    food_times = [3, 1, 2]
    k = 5
    print(solution(food_times, k))
