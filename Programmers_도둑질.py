# 나란히 인접한 두곳을 선택하지 않으면서 얻을 수 있는 최대 수익
def getMaxIncome(arr):
    n = len(arr)
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i])

    return dp[n-1]


def solution(money):
    if len(money) <= 3:  # 집이 세 개면 한집밖에 털지 못한다.
        return max(money)
    if len(money) == 4:  # 집이 네 개면 마주 보는 집의 합 중에서 큰 집 두곳을 턴다.
        return max(money[0]+money[2], money[1]+money[3])

    # 최대 수익을 얻을 수 있는 선택지 세 가지
    selectFirstHouse = money[0] + getMaxIncome(money[2:-1])  # 0번째 집 털 때
    selectLastHouse = money[-1] + getMaxIncome(money[1:-2])  # 1번째 집 털 때
    selectSecondHouse = money[1] + getMaxIncome(money[3:])  # 마지막 집 털 때

    return max(selectFirstHouse, selectSecondHouse, selectLastHouse)


if __name__ == "__main__":
    money = [1, 2, 3, 1]
    answer = solution(money)
    print(answer)
