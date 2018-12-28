# O(n^2) time | O(n) space
def min_number_of_jumps(arr):
    jumps = [float('inf') for x in arr]
    jumps[0] = 0
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[j] >= i - j:
                jumps[i] = min(jumps[i], jumps[j] + 1)
    return jumps[-1]
