# Best: O(n log n) time | O(n) space 
# Average: O(n log n) time | O(n) space 
# Worst: O(n log n) time | O(n) space
def merge_sort(array):
    if len(array) <= 1:
        return array
    aux_array = array[:]
    _merge_sort(array, 0, len(array) - 1, aux_array)
    return array

def _merge_sort(array, start, end, aux_array):
    if start == end:
        return
    middle = (start + end) // 2
    _merge_sort(aux_array, start, middle, array)
    _merge_sort(aux_array, middle+1, end, array)
    merge(array, start, middle, end, aux_array)

def merge(array, start, middle, end, aux_array):
    i = start
    j = middle + 1
    k = start
    while i <= middle and j <= end:
        if aux_array[i] <= aux_array[j]:
            array[k] = aux_array[i]
            i += 1
        else:
            array[k] = aux_array[j]
            j += 1
        k += 1
    while i <= middle:
        array[k] = aux_array[i]
        i += 1
        k += 1
    while j <= end:
        array[j] = aux_array[j]
        j += 1
        k += 1
