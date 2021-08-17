def solution(n):
    dp = [0] * (n+1)

    # 1칸 전에서 1칸을 점프하는 경우 + 2칸 전에서 2칸을 점프하는 경우의 수
    for i in range(1, n+1):
        if i == 1: dp[i] = 1
        elif i == 2: dp[i] = 2
        else: dp[i] = (dp[i-1] + dp[i-2]) % 1234567

    return dp[n]
