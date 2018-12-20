# O(log N) time | O(log N) space
def binary_search(array, target):
    return _binary_search(array, target, 0, len(array) - 1)

def _binary_search(array, target, low, high):
    if low > high:
        return -1
    middle = (low + high) // 2
    potential_match = array[middle]
    if potential_match == target:
        return middle
    if target < potential_match:
        return _binary_search(array, target, left, middle-1)
    return _binary_search(array, target, middle+1, high)
