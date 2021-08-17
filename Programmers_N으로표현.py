def solution(N, number):
    # 괄호 연산을 그냥 맨 앞으로 가져와서 한다고 가정
    # 할 수 있는 방법은 +, -, *, //, 자릿수늘리기

    numberMade = [[] for _ in range(9)]
    numberMade[1].append(N)  # 맨 처음 주어진 N을 삽입
    if N == number:
        return 1
    for i in range(2, 9):  # N을 i개 사용해서 만들 수 있는 조합은 (1, i-1), (2,i-2)...
        now = [int(str(N)*i)]  # N을 i개 이어 붙이는 경우
        for j in range(1, i // 2 + 1):
            cache1, cache2 = numberMade[j], numberMade[i-j]
            for x in cache1:
                for y in cache2:
                    if y != 0:
                        now.append(x//y)
                    if x != 0:
                        now.append(y//x)
                    now.extend([x+y, x-y, y-x, y*x])  # 항상 가능함
            if number in now:
                return i
        numberMade[i] = now
    return -1


if __name__ == "__main__":
    N = 4
    number = 17
    result = solution(N, number)
    print(result)
