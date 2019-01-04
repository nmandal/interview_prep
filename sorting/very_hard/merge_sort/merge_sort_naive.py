# Best: O(n log n) time | O(n log n) space 
# Average: O(n log n) time | O(n log n) space 
# Worst: O(n log n) time | O(n log n) space
def merge_sort(array):
    if len(array) == 1:
        return array
    middle_idx = len(array) // 2
    left = array[:middle_idx]
    right = array[middle_idx:]
    return merge_sorted_arrays(merge_sort(left), merge_sort(right))

def merge_sorted_arrays(left, right):
    sorted_array = [None] * (len(left) + len(right))
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array[k] = left[i]
            i += 1
        else:
            sorted_array[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        sorted_array[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        sorted_array[k] = right[j]
        j += 1
        k += 1
    return sorted_array
