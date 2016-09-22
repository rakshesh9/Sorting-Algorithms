def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
 
    if left < n and array[i] < array[left]:
        largest = left
 
    if right < n and array[largest] < array[right]:
        largest = right
 
    if largest != i:
        array[i],array[largest] = array[largest],array[i] 
        heapify(array, n, largest)

def maxheapify(array):
    n = len(array)

    # Maxheap.
    for i in range(n, -1, -1):
        heapify(array, n, i)
 
    # One by one extract elements
    for i in range(n-1, -1, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
 
array = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
maxheapify(array)
print(array)