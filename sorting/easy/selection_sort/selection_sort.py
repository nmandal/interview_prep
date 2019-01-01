# Best: O(n^2) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def selection_sort(arr):
    curr = 0
    while curr < len(arr) - 1:
        small = curr
        for i in range(curr + 1, len(arr)):
            if arr[small] > arr[i]:
                small = i
        swap(curr, small, arr)
        curr += 1
    return arr

def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]
