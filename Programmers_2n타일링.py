def solution(n):
    memo = []
    cache = [0 for index in range(n + 1)]
    cache[0] = 1
    cache[1] = 2

    for index in range(2, n+1):
        cache[index] = cache[index - 1] + cache[index - 2]
        cache[index] = cache[index] % 1000000007
    print(cache[n-1])
    return cache[n-1]


solution(10)
