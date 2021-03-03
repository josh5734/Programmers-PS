def solution(s):
    if len(s) == 1:
        return 1
    stringCompressionLength = []  # 압축된 문자열의 길이를 담는 리스트
    # 문자열 압축을 1~(문자열 길이의 절반)까지 해본다.
    for l in range(1, (len(s)//2+1)):
        compressedStack = []
        cursor = 0
        count = 1
        while cursor < len(s):
            nextString = s[cursor:cursor+l]
            if len(compressedStack) == 0:  # 스택에 아무것도 없으면 그냥 삽입
                compressedStack.append(count)
                compressedStack.append(nextString)
            elif compressedStack[-1] == nextString:  # 이전 문자와 현재 문자가 같다면 반복
                compressedStack[-2] += 1  # 반복되는 카운트를 1 증가시킨다.
            else:
                compressedStack.append(count)  # 이전 문자와 현재 문자가 다르면 그냥 삽입
                compressedStack.append(nextString)
            cursor += l  # 반복되는 문자열의 길이 l만큼 커서 이동
        # 스택에서 1 제거
        compressedStack = map(
            str, list(filter(lambda x: x != 1, compressedStack)))
        compressedString = ''.join(compressedStack)
        stringCompressionLength.append(len(compressedString))

    return min(stringCompressionLength)


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
