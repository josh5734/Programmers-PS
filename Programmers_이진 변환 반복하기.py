
def binaryTranslate(x, tanslateCount, zeroCount):
    # 종료조건 x == 1
    if x == '1':
        return tanslateCount, zeroCount

    # 모든 0을 제거
    numOfZeroes = x.count('0')
    x = '1' * (len(x) -numOfZeroes)
    zeroCount += numOfZeroes

    # x는 x의 길이 c를 이진법으로 표현한 문자열
    x = bin(len(x))[2:]
    
    return binaryTranslate(x, tanslateCount+1, zeroCount)

def solution(s):
    return list(binaryTranslate(s, 0, 0))



s = "110010101001"
print(solution(s))