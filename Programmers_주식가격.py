def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for index, p in enumerate(prices):
        # 처음에 비어 있으면 삽입 / 넣을 때 자신의 인덱스 정보를 함께 삽입
        if len(stack) == 0:
            stack.append((p, index))

        # 지금 넣을 주식 가격이 기존의 가격보다 크거나 같으면 그냥 삽입
        elif p >= stack[-1][0]:
            # 그 전에 주식들은 가격이 떨어지고 않고 있는 시간을 더하기
            for s in stack:
                answer[s[1]] += 1
            stack.append((p, index))

        # 지금 넣은 주식 가격이 하락세라면 그 전에 자신보다 높았던 가격들을 다 pop
        elif p < stack[-1][0]:
            while len(stack) != 0 and p < stack[-1][0]:
                answer[stack[-1][1]] += 1
                stack.pop()
            for s in stack:
                answer[s[1]] += 1
            stack.append((p, index))
    print(answer)

    return answer


solution([1, 3, 5, 2, 1])
