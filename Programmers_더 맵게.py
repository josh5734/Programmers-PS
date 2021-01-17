def heapify(scoville, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index < heap_size and scoville[left_index] > scoville[largest]:
        largest = left_index
    if right_index < heap_size and scoville[right_index] > scoville[largest]:
        largest = right_index

    if largest != index:
        scoville[largest], scoville[index] = scoville[index], scoville[largest]
        heapify(scoville, largest, heap_size)


def heap_sort(scoville):
    n = len(scoville)  # 20개

    for i in range(n // 2 - 1, -1, -1):  # largest의 index값은 n//2-1개 만큼 존재함. n = 20 이라면, index는 0~9이고, 자식노드는 20까지!
        heapify(scoville, i, n)  # largest = 10부터 / heapsize는 자료 개수만큼!

    for i in range(n - 1, 0, -1):
        scoville[0], scoville[i] = scoville[i], scoville[0]
        heapify(scoville, 0, i)
    return scoville


def solution(scoville, K):
    answer = 0
    scoville = heap_sort(scoville)

    max_scoville = sum(scoville)
    if max_scoville < K:
        return -1

    while len(scoville) > 1:
        scoville.append(scoville[0] + scoville[1] * 2)
        heap_sort(scoville)
        scoville = scoville[2:]
        answer += 1
        if scoville[0] >= K:
            break

    return answer