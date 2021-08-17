def solution(n):
    answer = 0

    # Greedy -> n부터 시작해서 짝수는 무조건 그 절반에서 순간이동
    # 홀수일때는 그 전 칸이 짝수칸 이므로 +1만 점프
    while n >= 1:
        if n % 2 == 0:
            n //= 2
        else:
            answer += 1
            n -= 1
    return answer