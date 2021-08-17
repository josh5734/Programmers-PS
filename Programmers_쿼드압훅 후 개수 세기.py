def quadTree(arr, x, y, length, answer):
    start = arr[x][y]
    flag = True
    for i in range(x, x + length):
        for j in range(y, y + length):
            # 하나라도 다른 수가 있으면 4개로 쪼개서 재귀 호출
            if start != arr[i][j]:
                length //= 2
                quadTree(arr, x, y, length, answer)
                quadTree(arr, x, y + length, length, answer)
                quadTree(arr, x + length, y, length, answer)
                quadTree(arr, x + length, y + length, length, answer)
                flag = False
                break
        # 다르다면 반복문 탈출
        if not flag:
            break
    # 모든 수가 같다면 카운트해주기
    if flag:
        if start == 0: answer[0] += 1
        elif start == 1: answer[1] += 1

def solution(arr):
    answer = [0,0]
    quadTree(arr, 0, 0, len(arr), answer)
    return answer




arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
print(solution(arr))
