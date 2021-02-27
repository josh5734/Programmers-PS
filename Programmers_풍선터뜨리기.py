# 풍선을 터뜨릴 때는 인접한 것끼리 터뜨려야 하기 때문에 정렬 X
# 어떤 수를 기준으로 왼쪽과 오른쪽에 자신보다 작은 값이 동시에 있으면 안된다.. -> 양쪽을 다 확인하려면 O(N^2)
# 양방향에서 하나씩 오면서 최소값을 체크

def solution(a):
    answer = []
    left_min, right_min = a[0], a[-1]
    length = len(a)
    # 현재 최소값이 위치한 위치
    min_index = a.index(min(a))

    # 각 값을 기준으로 양방향에 최소값을 구해보자.
    for i in range(0, min_index):
        left_min = a[i] if a[i] < left_min else left_min
        if left_min == a[i]:
            answer.append(a[i])

    for i in range(length-1, min_index-1, -1):
        right_min = a[i] if a[i] < right_min else right_min
        if right_min == a[i]:
            answer.append(a[i])

    return len(answer)


if __name__ == "__main__":

    a = [-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]
    a2 = [9, -1, -5]
    a3 = [1, -1, 2, -2, 3, -3]
    a4 = [-1, -2, 1, 2]
    a5 = [9, -1, -5]
    print(solution(a))
    print(solution(a2))
    print(solution(a3))
