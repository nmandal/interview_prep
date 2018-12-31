# O(log n) time | O(log n) space
def search_for_range(arr, target):
    final_range = [-1, -1]
    _altered_binary_search(arr, target, 0, len(arr) - 1, final_range, True)
    _altered_binary_search(arr, target, 0, len(arr) - 1, final_range, False)
    return final_range

def _altered_binary_search(arr, target, left, right, final_range, go_left):
    if left > right:
        return
    middle = (left + right) // 2
    if arr[middle] < target:
        _altered_binary_search(arr, target, middle+1, right, final_range, go_left)
    elif arr[middle] > target:
        _altered_binary_search(arr, target, left, middle-1, final_range, go_left)
    else:
        if go_left:
            if middle == 0 or arr[middle-1] != target:
                final_range[0] = middle
            else:
                _altered_binary_search(arr, target, left, middle-1, final_range, go_left)
        else:
            if middle == len(arr) - 1 or arr[middle+1] != target:
                final_range[1] = middle
            else:
                _altered_binary_search(arr, target, middle+1, right, final_range, go_left)
