def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    # Swap largest to father node -> Heapify swapped pos
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)

def heapSort(arr, n):
    for i in range(n//2 - 1, -1, -1):
        # Heapify in all non-leaf nodes -> Build max heap
        heapify(arr, n, i)

    for i in range(n-1, -1, -1):
        # Swap first node (largest) with last node -> First node now in right pos
        arr[0], arr[i] = arr[i], arr[0]
        # Re-heapify since first node, abandon right pos nodes
        heapify(arr, i, 0)

arr = [3, 2, 1, 4, 2, 9, 8]
heapSort(arr, len(arr))
print(arr)