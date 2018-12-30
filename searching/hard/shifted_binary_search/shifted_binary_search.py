# O(log n) time | O(log n) space
def shifted_binary_search(arr, target):
    _shifted_binary_search(arr, target, 0, len(arr) - 1)
    
def _shifted_binary_search(arr, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    pot_match = arr[middle]
    left_num = arr[left]
    right_num = arr[right]
    if target == pot_match:
        return middle
    elif left_num <= pot_match:
        if target < pot_match and target >= left_num:
            return _shifted_binary_search(arr, target, left, middle-1)
        return _shifted_binary_search(arr, target, middle+1, right)
    else:
        if target > pot_match and target <= right_num:
            return _shifted_binary_search(arr, target, middle+1, right)
        return _shifted_binary_search(arr, target, left, middle-1)
