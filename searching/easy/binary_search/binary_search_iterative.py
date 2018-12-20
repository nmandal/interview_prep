# O(log N) time | O(1) space
def binary_search(array, target):
    low = 0
    high = len(array) - 1
    
    while low <= high:
        middle = (low + high) // 2
        potential_match = array[middle]
        if potential_match == target:
            return middle
        if target < potential_match:
            high = middle - 1
        else:
            low = middle + 1
    return -1
