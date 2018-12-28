# O(n) time | O(1) space
def subarray_sort(arr):
    min_ooo = float('inf')
    max_ooo = float('-inf')
    for i, num in enumerate(arr):
        if is_ooo(i, num, arr):
            min_ooo = min(min_ooo, num)
            max_ooo = max(max_ooo, num)
    if min_ooo == float('inf'):
        return [-1, -1]
    left = 0
    right = len(arr)
    while min_ooo >= arr[left]:
        left += 1
    while max_ooo <= arr[right]:
        right -= 1
    return [left, right]

def is_ooo(i, num, arr):
    if i == 0:
        return num > arr[i+1]
    if i == len(arr) - 1:
        return num < arr[i-1]
    return num > arr[i+1] or num < arr[i-1]
