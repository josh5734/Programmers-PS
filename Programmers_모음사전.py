from itertools import product

def solution(word):
    alphabets = ["A","E","I","O","U"]
    dictionary = []

    # 중복 순열로 길이 = 1~5인 단어를 모두 구한다
    for i in range(1, 6):
        for w in list(product(alphabets,repeat=i)):
            dictionary.append(''.join(w))
    dictionary.sort()
    return dictionary.index(word)+1

print(solution(word = "EIO"))