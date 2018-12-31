# Best: O(n) time    | O(1) space
# Avg: O(n) time     | O(1) space
# Worst: O(n^2) time | O(1) space
def quickselect(arr, k):
    position = k - 1
    return _quickselect(arr, 0, len(arr) - 1, position)
    
def _quickselect(arr, start, end, position):
    while True:
        if start > end:
            raise Exception("Your algorithm should never arrive here")
        pivot = start
        left = start + 1
        right = end
        while left <= right:
            if arr[left] > arr[pivot] and arr[right] < arr[pivot]:
                swap(arr, left, right)
            if arr[left] <= arr[pivot]:
                left += 1
            if arr[right] >= arr[pivot]:
                right -= 1
        swap(arr, pivot, right)
        if right == position:
            return arr[right]
        elif right < position:
            start = right + 1
        else:
            end = right - 1
               
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
