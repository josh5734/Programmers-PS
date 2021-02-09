def binary_search(stones, left, right, k):
    answer = 0
    while left <= right:
        mid = (left + right) // 2

        blank = 0

        for i in range(len(stones)):
            # 연속으로 k칸이상 음수가 되면 건널 수 없음 - 종료
            if stones[i] - mid < 0:
                blank += 1
                if blank == k:
                    break
            else:
                blank = 0

        if blank == k:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid
    return answer


def solution(stones, k):

    left, right = 0, int(1e10)
    answer = binary_search(stones, left, right, k)
    return answer


if __name__ == "__main__":
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3

    result = solution(stones, k)
    print(result)


# 효율성 테스트 실패 #####################3
'''
def solution(stones, k):
    answer = 0
    # 시작과 끝 위치 설정
    stones.insert(0, 0)
    stones.append(-1)
    length = len(stones)
    while True:
        # 징검다리를 건너기 전 위치를 0으로 두고 시작
        cursor = 0

        # 끝까지 도착하기 전까지 while loop 수행
        while cursor < length-1:
            cross = False
            # 한칸부터 k칸까지 이동할 곳이 있다면 이동
            for i in range(1, k+1):
                if stones[cursor+i] > 0:
                    cursor += i
                    stones[cursor] -= 1
                    cross = True
                    break
                elif stones[cursor+i] == -1:
                    cursor += i
                    cross = True
                    break
            # 현재에서 갈 곳이 없으면 종료
            if not cross:
                return answer
        # 다 건너면 정답에 +1
        answer += 1

    return answer
'''
