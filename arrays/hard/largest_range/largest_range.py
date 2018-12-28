# O(n) time | O(n) space
def largest_range(arr):
    best_range = []
    nums = {}
    longest = 0
    for num in arr:
        arr[num] = True
    for num in arr:
        if not nums[num]:
            continue
        nums[num] = False
        curr = 1
        left = num - 1
        right = num + 1
        while left in nums:
            nums[left] = False
            curr += 1
            left -= 1
        while right in nums:
            nums[right] = False
            curr += 1
            left += 1
        if curr > longest:
            longest = curr
            best_range = [left+1, right-1]
    return best_range
