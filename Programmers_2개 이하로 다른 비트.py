def solution(numbers):
    answer = []
    for number in numbers:
        # number를 bit로 바꿔서 0, 1만 관찰하자
        numberBit = list(bin(number)[2:])
        zero_pos, one_pos = -1, []
        for b in range(len(numberBit)):
            # 가장 뒤쪽에 있는 0과 1의 위치 저장
            if numberBit[b] == '0':
                zero_pos = b
            if numberBit[b] == '1':
                one_pos.append(b)
                
        # 0이 한 개라도 존재한다면 1로 바꿀 수 있다.
        if zero_pos >= 0:
            numberBit[zero_pos] = '1'
            # 0 다음에 가장 가까운 1을 0으로 바꾼다.
            for p in one_pos:
                if p > zero_pos:
                    numberBit[p] = '0'
                    break
            numberBit = ''.join(numberBit)
        # 0이 한 개도 없으면 맨 앞에 1을 붙이고 그 다음에 1은 0으로 바꾼다.
        else:
            numberBit = '10' + ''.join(numberBit[1:])
        answer.append(int(numberBit, 2))

    return answer

a = [343]
numbers = [1001,337,0,1,333,673,343,221,898,997,121,1015,665,779,891,421,222,256,512,128,100]
print(solution(numbers))
