# O(n) time | O(1) space
def min_number_of_jumps(arr):
    if len(arr) == 1:
        return 0
    jumps = 0
    max_reach = arr[0]
    steps = arr[0]
    for i in range(1, len(arr) - 1):
        max_reach = max(max_reach, i + arr[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = max_reach - i
    return jumps + 1
