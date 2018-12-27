# O(n^2) time | O(n) space
def max_sum_increasing_subsequence(arr):
    sums = [None for x in arr]
    seqs = [num for num in arr]
    max_sum_idx = 0
    for i in range(len(arr)):
        curr_num = arr[i]
        for j in range(0, i):
            other_num = arr[j]
            if other_num < curr_num and sums[j] + curr_num >= sums[i]:
                sums[i] = sums[j] + curr_num
                seqs[i] = j
        if sums[i] >= sums[max_sum_idx]:
            max_sum_idx = i
    return [sums[max_sum_idx], build_sequence(arr, seqs, max_sum_idx)]

def build_sequence(arr, seqs, curr_idx):
    seq = []
    while curr_idx is not None:
        seq.append(arr[curr_idx])
        curr_idx = seqs[curr_idx]
    return list(reversed(seq))
