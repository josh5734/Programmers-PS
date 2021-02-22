from collections import defaultdict


def dfs(start, flight, answer):
    stack = [start]
    while stack:
        now = stack[-1]

        # 특정 도시에서 갈 곳이 없으면 answer에 삽입
        if not flight.get(now) or len(flight[now]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(flight[now].pop(0))


def solution(tickets):
    answer = []
    flight = defaultdict(list)

    # 항공편의 정보를 딕셔너리 형태로 입력받기
    for i in range(len(tickets)):
        start, end = tickets[i][0], tickets[i][1]
        flight[start].append(end)

    # 알파벳 순서대로 정렬
    for v in flight.values():
        v.sort()
    dfs("ICN", flight, answer)

    return answer[::-1]


if __name__ == "__main__":
    tickets1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    tickets2 = [["ICN", "SFO"], ["ICN", "ATL"], [
        "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    tickets3 = [["ICN", "A"], ["ICN", "B"], [
        "A", "D"], ["D", "A"], ["B", "ICN"]]
#    print(solution(tickets1))
    print(solution(tickets2))
    print(solution(tickets3))
