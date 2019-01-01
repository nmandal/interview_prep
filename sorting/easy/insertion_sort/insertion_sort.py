# Best: O(n) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            swap(j, j-1, arr)
            j -= 1
    return arr

def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]
