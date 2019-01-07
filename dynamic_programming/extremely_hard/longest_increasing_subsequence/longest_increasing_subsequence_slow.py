# O(n^2) time | O(n) space
def longest_increasing_subsequence(array):
    seqs = [None for x in array]
    lengths = [1 for x in array]
    max_length_idx = 0
    for i in range(len(array)):
        curr = array[i]
        for j in range(0, i):
            other = array[j]
            if other < curr and lengths[j] + 1 >= lengths[i]:
                lengths[i] = lengths[j] + 1
                seqs[i] = j
        if lengths[i] >= lengths[max_length_idx]:
            max_length_idx = i
    return build_sequence(array, seqs, max_length_idx)

def build_sequence(array, seqs, max_length_idx):
    seq = []
    while max_length_idx is not None:
        seq.append(array[max_length_idx])
        max_length_idx = seqs[max_length_idx]
    return list(reversed(seq))
