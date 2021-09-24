from itertools import permutations as P

def splitExpression(expression, sep):
    numbers, operations, integer = [], [], ""
    for s in expression:
        if s in sep:
            numbers.append(int(integer))
            operations.append(s)
            integer = ""
        else:
            integer += s
    numbers.append(int(integer))

    return numbers, operations

def solution(expression):
    # 연산자 종류
    sep = ['*', '+', '-']
    
    # 주어진 expression을 숫자와 연산자로 구분해서 저장할 리스트
    numbers, operations = splitExpression(expression, sep)

    answer = 0
    # 가능한 모든 조합에 대해 우승 상금을 정해본다.
    for priority_ops in list(P(sep, 3)):
        temp_num, temp_op = numbers[:], operations[:]

        # 연산자 우선순위의 순열을 각각 조회
        for op in priority_ops:
            # 우선순위를 갖는 연산자부터 전부 연산을 수행해본 후 결과값 저장
            while True:
                try:
                    opIndex = temp_op.index(op)
                    temp_op.pop(opIndex)
                    left = temp_num.pop(opIndex)
                    right = temp_num.pop(opIndex)

                    if op == "+":
                        temp_num.insert(opIndex, left + right)
                    elif op == "-":
                        temp_num.insert(opIndex, left - right)
                    else:
                        temp_num.insert(opIndex, left * right)
                except:
                    break

        # 최종 계산 결과가 최대값을 갖는지 확인
        result = abs(temp_num[0])
        if result > answer:
            answer = result
    return answer


print(solution(expression = "50*6-3*2"))

