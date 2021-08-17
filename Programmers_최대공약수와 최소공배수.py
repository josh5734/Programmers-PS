def solution(n, m):
    answer = [1]

    for i in range(1, n + 1):
        if (n % i == 0 and m % i == 0):
            answer[0] = i  # i는 마지막꺼로 대체되지..

    max_list1 = []
    max_list2 = []
    k = n * m
    for p in range(1, k + 1):
        if k % p == 0:
            max_list1.append(p)

    for q in max_list1:
        if (q % n == 0 and q % m == 0):
            max_list2.append(q)
    answer.append(min(max_list2))
    return answer
    print(answer)