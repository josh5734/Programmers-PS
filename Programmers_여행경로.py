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
    print(solution(tickets1))
    print(solution(tickets2))
    print(solution(tickets3))

'''
###### 테스트케이스 1번만 안되는데 반례를 찾으려고 해도 도저히 찾을수가 없음 #####

def visit(start, flight, answer):
    answer.append(start)
    if not flight.get(start) or len(flight[start]) == 0:
        return answer

    temp = flight[start][0][0]
    flight[start].pop(0)
    start = temp
    visit(start, flight, answer)


def solution(tickets):
    answer = []
    flight = defaultdict(list)

    # 항공편의 정보를 딕셔너리 형태로 입력받기
    # 도착지로부터 시작지로 다시 오는 티켓이 있는 것과 없는 것 구분
    for i in range(len(tickets)):
        start, end = tickets[i][0], tickets[i][1]
        count = 0
        for j in range(len(tickets)):
            tmp_start, tmp_end = tickets[j][0], tickets[j][1]
            if i != j and start == tmp_end and end == tmp_start:
                count = 1
        flight[start].append([end, count])

    # 왕복있는 티켓먼저 -> 알파벳 순서 정렬
    for k in flight:
        flight[k] = sorted(flight[k], key=lambda x: (-x[1], x[0]))
    visit("ICN", flight, answer)
    return answer


'''
