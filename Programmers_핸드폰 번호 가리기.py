def solution(phone_number):
    n = len(phone_number)
    phone_number = list(phone_number)
    for i in range(n-4):
        phone_number[i] = "*"
    answer = ''.join(phone_number)
    return answer
    print(answer)