# 열쇠가 자물쇠에 들어맞는지 확인하는 함수
def check(dx, dy, key, lock_o, lock_x):
    m = len(key)
    check = True
    # 열쇠의 홈, 돌기의 정보를 각각 리스트에 담는다.
    key_o, key_x = [], []
    for i in range(m):
        for j in range(m):
            if key[i][j] == 1:
                key_o.append((i, j))
            else:
                key_x.append((i, j))

    # 만약 자물쇠의 홈 부분이 키의 돌기에 다 없으면 False
    for x, y in lock_x:
        if (x+dx, y+dy) not in key_o:
            check = False
    # 만약 자물쇠의 돌기 부분이 키의 돌기 부분과 겹치면 False
    for x, y in lock_o:
        if (x+dx, y+dy) in key_o:
            check = False
    return check
# 열쇠를 90도 회전하는 함수


def rotate90(key):
    m = len(key)
    key90 = [[0 for _ in range(m)] for _ in range(m)]

    for i in range(m):
        for j in range(m):
            key90[i][j] = key[j][m-i-1]
    return key90

# 열쇠를 180도 회전하는 함수


def rotate180(key):
    m = len(key)
    key180 = [[0 for _ in range(m)] for _ in range(m)]

    for i in range(m):
        for j in range(m):
            key180[i][j] = key[m-i-1][m-j-1]
    return key180

# 열쇠를 270도 회전하는 함수


def rotate270(key):
    m = len(key)
    key270 = [[0 for _ in range(m)] for _ in range(m)]

    for i in range(m):
        for j in range(m):
            key270[i][j] = key[m-j-1][i]
    return key270


def solution(key, lock):
    m = len(key)
    n = len(lock)
    # 열쇠를 회전하고 들어맞는지 확인
    key90 = rotate90(key)
    key180 = rotate180(key)
    key270 = rotate270(key)

    # 자물쇠의 홈, 돌기의 정보를 따로 리스트에 담기
    lock_o, lock_x = [], []
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                lock_x.append((i, j))
            else:
                lock_o.append((i, j))

    for dx in range(-n, n):
        for dy in range(-n, n):
            # 원래, 90도, 180도, 270도 키를 돌려서 확인
            if check(dx, dy, key, lock_o, lock_x) == True or check(dx, dy, key90, lock_o, lock_x) == True or check(dx, dy, key180, lock_o, lock_x) == True or check(dx, dy, key270, lock_o, lock_x) == True:
                return True
    return False


if __name__ == "__main__":
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution(key, lock))
