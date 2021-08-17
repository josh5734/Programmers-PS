from collections import deque


def bfs(begin_idx, target_idx, words_graph, visited):
    q = deque()
    q.append(begin_idx)
    visited[begin_idx] = True
    count = 0
    # 이렇게 while문 2개써서 count해야 되는건가....?
    while True:
        # 현재 단어에서 될 수 있는 다른 단어들
        temp = []
        while q:
            now = q.popleft()
            for x in words_graph[now]:
                if visited[x] == False:
                    visited[x] = True
                    temp.append(x)
        count += 1
        q.extend(temp)
        # 현재 단어에서 변환 가능한 것이 없다면 종료
        if not q:
            return 0
        # 현재 단어에 목표하는 단어가 있다면 count를 return
        if target_idx in q:
            return count

    return 0


def make_graph(words, length):
    words_graph = [[] for _ in range(length)]

    for i in range(length-1):
        start_word = words[i]
        for j in range(i+1, length):
            end_word = words[j]
            temp = 0
            # 두 단어가 한 자리만 다르다면 서로 연결
            for a, b in zip(start_word, end_word):
                if a != b:
                    temp += 1
            if temp == 1:
                words_graph[i].append(j)
                words_graph[j].append(i)
    return words_graph


def solution(begin, target, words):
    # 시작단어를 words에 삽입
    words.insert(0, begin)
    length = len(words)
    # begin의 index = 0
    begin_idx = 0
    # target의 index 정하기
    target_idx = -1
    for i in range(length):
        if words[i] == target:
            target_idx = i
            break

    # 단어들을 undirected 그래프 형태로 연결
    words_graph = make_graph(words, length)

    # BFS 수행
    visited = [False] * length
    answer = bfs(begin_idx, target_idx, words_graph, visited)
    return answer


if __name__ == "__main__":

    begin = "hit"
    target = "cog"
    words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
    words2 = ['hot', 'cot', 'cog']
    print(solution(begin, target, words2))
