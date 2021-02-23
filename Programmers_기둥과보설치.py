import copy


def show(building):
    length = len(building)
    for i in range(length):
        for j in range(length):
            print(building[i][j], end=' ')
        print()
# 기둥 설치 - 바닥 위에 있거나, 보의 한쪽 끝 부분에 있거나, 다른 기둥 위에 있어야 한다.


def build_wall(x, y, building):
    if y == len(building) - 2:  # 지면에 세우는 경우
        building[y][x] = 'W'
        return True
    elif building[y+1][x] == 'W':
        if building[y][x] == 'P':  # 기둥 위에 보가 설치되어 있고 그 위에 기둥을 세우는 경우
            building[y][x] = 'PW'
        else:  # 그냥 기둥 위에 기둥을 세우는 경우
            building[y][x] = 'W'
        return True

    elif building[y][x] == 'P':
        building[y][x] = 'PW'
        return True

    elif building[y][x-1] in 'PW' or building[y][x+1] in 'PW':  # 보 끝에 기둥을 세우는 경우
        building[y][x] = 'W'
        return True
    return False


def delete_wall(x, y, building):  # 기둥 삭제 - 기존에 존재하던 기둥이나 보에 영향을 주면 안된다.
    test = copy.deepcopy(building)
    # 기존에 있던 기둥을 삭제해본다.
    if test[y][x] == 'PW':
        test[y][x] = 'P'
    elif test[y][x] == 'W':
        test[y][x] = 'X'

    if test[y-1][x] == 'W':
        if build_wall(x, y-1, test) == True:
            building[y][x] = 'X'
    elif test[y-1][x] == 'P':
        if build_paper(x, y-1, test) == True:
            building[y][x] = 'X'
    elif test[y-1][x] == 'PW':
        if build_paper(x, y-1, test) == True and build_wall(x, y-1, test) == True:
            building[y][x] = 'X'
    elif test[y-1][x] == 'X':
        building[y][x] = 'X'

# 보 설치 - 한쪽 끝 부분이 기둥 위에 있거나, 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 한다.


def build_paper(x, y, building):

    if building[y+1][x] == 'W':
        if building[y][x] == 'W':
            building[y][x] = 'PW'
        else:
            building[y][x] = 'P'
        return True

    elif building[y+1][x+1] == 'W' or building[y+1][x-1] == 'W':  # 보의 오른쪽이나 왼쪽 끝에 기둥이 있는 경우
        building[y][x] = 'P'
        return True

    elif building[y][x-1] == 'P' and building[y][x+1] == 'P':  # 보의 왼쪽 오른쪽 모두 보가 설치되어 있는 경우
        building[y][x] = 'P'
        return True
    return False


def delete_paper(x, y, building):  # 보 삭제 - 기존에 존재하던 기둥이나 보에 영향을 주면 안된다.
    test = copy.deepcopy(building)
    # 기존에 있던 보를 삭제해본다.
    if test[y][x] == 'PW':
        test[y][x] = 'W'
    elif test[y][x] == 'P':
        test[y][x] = 'X'

    if test[y-1][x] == 'W':
        if build_wall(x, y-1, test) == True:
            building[y][x] = 'X'
    elif test[y][x-1] == 'P':
        if build_paper(x, y-1, test) == True:
            building[y][x] = 'X'
    # elif test[y-1][x] == 'PW':
    #     if build_paper(x, y-1, test) == True and build_wall(x, y-1, test) == True:
    #         building[y][x] = 'X'


def solution(n, build_frame):
    frame = []
    building = [['X'] * (n+2) for _ in range(n+2)]

    # 작업을 순서대로 입력받는다.
    for bf in build_frame:
        x, y, item, oper = bf[0], n-bf[1], bf[2], bf[3]
        # 기둥 설치
        if item == 0 and oper == 1:
            build_wall(x, y, building)
        # 기둥 삭제 -
        elif item == 0 and oper == 0:
            delete_wall(x, y, building)

        # 보 설치
        elif item == 1 and oper == 1:
            build_paper(x, y, building)

        # 보 삭제
        elif item == 1 and oper == 0:
            delete_paper(x, y, building)

    for i in range(n+2):
        for j in range(n+2):
            if building[i][j] == 'W':
                frame.append([j, 5-i, 0])
            elif building[i][j] == 'P':
                frame.append([j, 5-i, 1])
            elif building[i][j] == 'PW':
                frame.append([j, 5-i, 0])
                frame.append([j, 5-i, 1])

    frame = sorted(frame)
    # show(building)

    return frame


if __name__ == "__main__":
    n = 5
    x = [[0, 0, 0, 1], [0, 0, 0, 0]]
    build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [
        2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1], [5, 0, 0, 0]]
    build_frame2 = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [
        1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
    print(solution(n, build_frame))
    print(solution(n, build_frame2))
    print(solution(n, x))
