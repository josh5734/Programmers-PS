import math

# 정답 풀이 - 최대 공약수 활용
# 우선 w와 h가 공약수가 있다면 문제를 공약수를 나눈 w' 와 h'로 축소시킬 수 있다.
# w'와 h'가 서로소라 가정했을 때, 대각선은 반대쪽 코너에 도달하기전 w'-1 세로선과 h'-1 가로선을 지나고 지날때마다 새로운 정사각형이 추가된다.
# 그래서 첫 정사각형을 포함 1 + (w'-1) + (h'-1) = w' + h' - 1개의 정사각형을 지나게 되므로
# 공약수를 다시 곱해주면 w + h - gcd(w,h)개의 정사각형을 지나는것을 찾을 수 있다.


def solution(w, h):
    return w*h - w - h + math.gcd(w, h)


if __name__ == "__main__":
    w, h = 8, 12
    print(solution(w, h))


'''
########### 테스트케이스 13, 16 시간 초과 #############
def solution(w, h):
    if w == 1 or h == 1:
        return 0
    if w == h:
        return w*h - w
    answer = w*h-1
    # 가로, 세로중에 짧은 곳을 가로, 긴 곳을 세로로 고정
    w, h = min(w, h), max(w, h)

    # 한 행씩 내려갈때마다 격자가 x축방향으로 이동하는 길이
    dx = w / h
    for i in range(1, h):
        start, end = dx * i, dx * (i+1)
        # 끝부분이 모서리에 닿지 않고, 격자선이 한 변을 뚫고 지나갈 때는 두개가 날라감
        if i*dx - int(i*dx) != 0 and math.ceil(i * dx) != math.ceil((i+1)*dx):
            answer -= 2
        else:
            answer -= 1
    return answer
'''
