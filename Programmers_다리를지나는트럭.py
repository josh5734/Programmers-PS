from collections import deque


def solution(bridge_length, weight, truck_weights):
    onBridgeTrucks = deque()  # 현재 다리 위에 있는 트럭들
    onBridgeWeight = 0  # 현재 다리 위에 있는 트럭 무게의 합
    time = 0
    truck_weights = truck_weights[::-1]  # Queue로 만들기

    while(len(truck_weights) != 0 or len(onBridgeTrucks) != 0):  # 다리를 건너고 있거나, 건널 예정인 트럭이 잇는 동안
        time += 1  # 시간 경과
        for i in range(len(onBridgeTrucks)):
            onBridgeTrucks[i][1] += 1  # 다리 위의 트럭 이동
        if len(onBridgeTrucks) > 0:
            if onBridgeTrucks[0][1] > bridge_length:
                onBridgeWeight -= onBridgeTrucks.popleft()[0]  # 트럭 나가고 무게 감소
        if len(truck_weights) > 0:
            nextTruck = truck_weights[-1]
            if onBridgeWeight + nextTruck <= weight:
                # 트럭 위치 = 1로 초기화해서 append
                onBridgeTrucks.append([nextTruck, 1])
                onBridgeWeight += nextTruck  # 다리 위의 무게 증가
                truck_weights.pop()  # 대기 트럭에서 제거
    return time


if __name__ == "__main__":
    bridge_length = 100
    weight = 100
    truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    result = solution(bridge_length, weight, truck_weights)
    print(result)
