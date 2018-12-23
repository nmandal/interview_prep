# Time Complexity
#  Worst: O(N^2)
#  Best: O(N log N)
#  Average: O(N log N)
# Space Complexity: O(log N)
def quick_sort(array):
    _quick_sort(array, 0, len(array) - 1)

def _quick_sort(array, start, end):
    if start > end:
        return
    pivot = start
    left = start + 1
    right = end
    while right >= left:
        if array[left] > array[pivot] and array[right] < array[pivot]:
            swap(i, j, array)
        if array[left] <= array[pivot]:
            left += 1
        if array[right] >= array[pivot]:
            right -= 1
    swap(pivot, right, array)
    left_subarray_is_smaller = right - 1 - start < end - (right + 1)
    if left_subarray_is_smaller:
        _quick_sort(array, start, right - 1)
        _quick_sort(array, right + 1, end)
    else:
        _quick_sort(array, right + 1, end)
        _quick_sort(array, start, right - 1)
    
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
