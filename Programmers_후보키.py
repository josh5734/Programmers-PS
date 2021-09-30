from itertools import combinations as C

def solution(relation):
    # column의 개수 c <= 8, row의 개수 r <= 20 -> 완전탐색
    r, c = len(relation), len(relation[0])
    columnIndex = [i for i in range(c)]
    candidateKey = []

    # 가능한 모든 키 조합에 대해
    for i in range(1, c+1):
        for keyComb in list(C(columnIndex, i)):
            uniqueness = True
            chk = []

            # 릴레이션에서 해당 키의 튜플만 저장
            for rel in relation:
                temp = []
                for key in keyComb:
                    temp.append(rel[key])

                # 유일성 체크
                if temp in chk:
                    uniqueness = False
                    break
                else:
                    chk.append(temp)

            # 유일성 테스트를 통과한다면
            if uniqueness:
                # 최소성 체크
                currKey = ''.join(map(str,keyComb))
                minimality = True

                # 이전에 결정된 후보키를 모두 포함하는 키가 있다면 최소성 만족 X
                for existingKey in candidateKey:
                    count = len(existingKey)
                    for ek in existingKey:
                        for ck in currKey:
                            if ek == ck:
                                count -= 1
                    if count == 0:
                        minimality = False
                        break

                if minimality:
                    candidateKey.append(currKey)
    return len(candidateKey)


# print(solution(relation=[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
print(solution(relation=[["1","a","x"],["2","a","z"],["3","c","x"]]))
print(solution([['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']]))