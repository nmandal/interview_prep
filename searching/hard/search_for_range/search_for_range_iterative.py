# O(log n) time | O(1) space
def search_for_range(arr, target):
    final_range = [-1, -1]
    _altered_binary_search(arr, target, 0, len(arr) - 1, final_range, True)
    _altered_binary_search(arr, target, 0, len(arr) - 1, final_range, False)
    return final_range

def _altered_binary_search(arr, target, left, right, final_range, go_left):
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] < target:
            left = middle + 1
        elif arr[middle] > target:
            right = middle - 1
        else:
            if go_left:
                if middle == 0 or array[middle-1] != target:
                    final_range[0] = middle
                    return
                else:
                    right = middle - 1
            else:
                if middle == len(array) - 1 or array[middle+1] != target:
                    final_range[1] = middle
                    return
                else:
                    left = middle + 1
