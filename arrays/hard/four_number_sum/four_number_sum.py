# Average: O(n^2) time | O(n^2) space
# Worst: O(n^3) time | O(n^2) space
def four_number_sum(arr, target):
    pair_sums = {}
    quadruplets = []
    for i in range(1, len(arr) - 1):
        for j in range(i+1, len(arr)):
            curr = arr[i] + arr[j]
            diff = target - curr
            if diff in pair_sums:
                for pair in pair_sums[diff]:
                    quadruplets.append(pair + [arr[i], arr[j]])
        for k in range(0, i):
            curr = arr[i] + arr[k]
            if curr not in pair_sums:
                pair_sums[curr] = [[arr[k], arr[i]]]
            else:
                pair_sums[curr].append([arr[k], arr[i]])
        return quadruplets
