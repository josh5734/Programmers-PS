# 일차원 배열에서 연속해서 두 개를 뽑지 않았을 때 최대값을 구하는 dp
def normal_dp(sticker):
    n = len(sticker)
    if n <= 3:
        return max(sticker)
    
    dp = [0] * n
    dp[0] = sticker[0]
    dp[1] = max(sticker[0], sticker[1])
    
    for i in range(2, n):   
        dp[i] = max(dp[i-2] + sticker[i], dp[i-1])
    return max(dp)

def solution(sticker):
    n = len(sticker)

    # 스티커가 3장 이하인 경우
    if n <= 3:
        return max(sticker)
    
    # 1번 스티커를 선택한 경우
    # 마지막 스티커는 선택 X
    first_selected = normal_dp(sticker[2:-1]) + sticker[0]
    
    # 1번 스티커를 선택하지 않으면 # 2번 스티커부터 dp
    first_not_selected = normal_dp(sticker[1:])
    return max(first_selected, first_not_selected)