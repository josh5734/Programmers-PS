def solution(s):
    if len(s) == 1:
        return 1
    shortestLength = len(s)
    # 문자열 압축을 1~(문자열 길이의 절반)까지 해본다.
    for l in range(1, (len(s)//2+1)):
        compressedStack = []
        cursor = 0
        while cursor < len(s):
            nextString = s[cursor:cursor+l]
            # 스택에 아무것도 없거나, 이전 문자와 현재 문자가 다르면 1과 문자열을 삽입한다.
            if len(compressedStack) == 0 or compressedStack[-1] != nextString:
                compressedStack.append(1)
                compressedStack.append(nextString)
            # 이전 문자와 현재 문자가 같다면 반복되는 카운트를 1 증가시킨다.
            elif compressedStack[-1] == nextString:
                compressedStack[-2] += 1
            cursor += l  # 반복되는 문자열의 길이 l만큼 커서 이동
        # 스택에서 1 제거
        compressedStack = map(
            str, list(filter(lambda x: x != 1, compressedStack)))
        compressedString = ''.join(compressedStack)

        if len(compressedString) < shortestLength:
            shortestLength = len(compressedString)

    return shortestLength


if __name__ == "__main__":
    s1 = "aabbaccc"  # 2a2ba3c
    s2 = "ababcdcdababcdcd"
    s3 = "abcabcdede"
    s4 = "abcabcabcabcdededededede"
    s5 = "xababcdcdababcdcd"
    print(solution(s1))
    print(solution(s2))
    print(solution(s3))
    print(solution(s4))
    print(solution(s5))
    print(solution("aa"))
