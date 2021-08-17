def solution(name):

    name = list(name)
    answer = 0
    up_alpha = ["B", "C", "D", "E", "F", "G",
                "H", "I", "J", "K", "L", "M", "N"]
    down_alpha = ["O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    # 알파벳 바꾸기 횟수
    for i in name:
        if i in up_alpha:
            answer += up_alpha.index(i)+1
        elif i in down_alpha:
            answer += 12 - down_alpha.index(i)

    cursor_move = []
    a_idx, not_a_idx = [], []
    for i, alphabet in enumerate(name):
        if alphabet == "A":
            a_idx.append(i)
        else:
            not_a_idx.append(i)

    # not_a_idx 사이에는 "A"밖에 존재하지 않으므로 그 곳들을 기준으로 오른쪽으로 이동했다가 왼쪽으로 돌아가는 경우들을 list에 목록 담기
    for i in range(len(not_a_idx)-1):
        if len(not_a_idx) >= 2:
            cursor_move.append(not_a_idx[i]*2 + len(name)-not_a_idx[i+1])
        elif len(not_a_idx) == 1:
            cursor_move.append(not_a_idx[-1]*2 + len(name)-not_a_idx[-1])

    # 오른쪽으로만 이동하는 경우
    cursor_move.append(not_a_idx[-1])

    answer += min(cursor_move)

    return answer
