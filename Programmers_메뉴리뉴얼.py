from itertools import combinations as comb
from collections import Counter 

# orders 크기, 음식 숫자 고려하면 완전탐색 가능
def solution(orders, course):
    answer = []
    # 코스메뉴의 구성 수에 따라 loop
    for c in course:
        # 가능한 코스요리별 주문 횟수를 담는 리스트
        order_list = []
        for order in orders:

            # ABC -> 4개짜리 코스요리 x
            if len(order) >= c:
                for comb_order in comb(order, c):
                    order_list.append(''.join(sorted(comb_order)))  # 음식명을 정렬

        # 많이 주문된 순서대로 갯수를 세서 리스트 형태로 반환
        order_list = Counter(order_list).most_common()

        for menu, count in order_list:
            if count >= 2 and count == order_list[0][1]:    # 가장 긴 코스요리로만 구성
                answer.append(menu)
                
    return sorted(answer)



if __name__ == "__main__":
    orders =  ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2,3,4]
    print(solution(orders,course))