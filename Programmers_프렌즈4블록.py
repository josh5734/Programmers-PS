# 2 * 2블록이 삭제될 블록인지 확인
def check_remove(r, c, board, shape, check):
    if (shape == board[r][c+1] and shape == board[r+1][c] and shape == board[r+1][c+1]):
        check[r][c] = True
        check[r][c+1] = True
        check[r+1][c] = True
        check[r+1][c+1] = True


def solution(m, n, board):
    answer = 0
    board_list = [[] for _ in range(m)]
    for i in range(m):
        board_list[i] = list(board[i])

    while True:
        remove = False
        check = [[False]*n for _ in range(m)]
        # 삭제할 블록 체크
        for r in range(m-1):
            for c in range(n-1):
                shape = board_list[r][c]
                # 이미 삭제된 블록에 대해서는 체크하지 않는다.
                if shape != 'X':
                    check_remove(r, c, board_list, shape, check)

        # 블록 삭제
        for i in range(m):
            for j in range(n):
                # 삭제할 블록이 있다면 remove = True
                if check[i][j] == True:
                    remove = True
                    # 삭제되는 블록은 'X'로 표시
                    board_list[i][j] = 'X'
                    answer += 1

        # 더 이상 삭제할 블록이 없다면 종료
        if not remove:
            return answer

        # 위 블록 땡기기 // 각 Column별로 'X'표시된 것들을 다 앞으로 당기고 board_list에 반영한다.
        for c in range(n):
            temp_col = []
            for r in range(m):
                temp_col.append(board_list[r][c])
            for i in range(len(temp_col)):
                if temp_col[i] == 'X':
                    temp_col.pop(i)
                    temp_col.insert(0, 'X')

            for r in range(m):
                board_list[r][c] = temp_col[r]


if __name__ == "__main__":
    m, n = 6, 6
    board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

    answer = solution(m, n, board)
    print(answer)
