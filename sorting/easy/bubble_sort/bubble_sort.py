# Best: O(n) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def bubble_sort(arr):
    is_sorted = False
    counter = 0
    while not is_sorted:
        is_sorted = True
        for i in range(len(arr) - 1 - counter):
            if arr[i] > arr[i+1]:
                swap(i, i+1, arr)
                is_sorted = False
        counter += 1
    return arr

def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]
