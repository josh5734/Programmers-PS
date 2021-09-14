def solution(numbers, hand):
    answer = ''
    
    # 자판 정보와 초기 엄지 손가락 위치 입력받기
    left, right = [3,0], [3,2]
    board = dict()
    num = 1
    for i in range(3):
        for j in range(3):
            board[num] = [i,j]
            num += 1
    board[0] = (3,1)

    
    for num in numbers:
        
        # 숫자가 위치하는 배열의 인덱스
        x, y = board[num][0], board[num][1]
        
        if y == 0: # 1, 4, 7
            answer += "L"
            left = [x,y]

        elif y == 2: # 3, 6, 9
            answer += "R"
            right = [x,y]
        
        else: # 2, 5, 8, 0    
            left_distance = abs(y - left[1]) + abs(x-left[0])
            right_distance = abs(y-right[1]) + abs(x-right[0])
            
            if left_distance < right_distance:
                answer += "L"
                left = [x,y]
            elif left_distance > right_distance:
                answer += "R"
                right = [x,y]
            else:
                if hand == "right":
                    answer += "R"
                    right = [x,y]
                else:
                    answer += "L"
                    left = [x,y]
    
    return answer