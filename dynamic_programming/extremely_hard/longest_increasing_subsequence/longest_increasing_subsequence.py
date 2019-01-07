# O(nlogn) time | O(n) space
def longest_increasing_subsequence(array):
    seqs = [None for x in array]
    indicies = [None for x in range(len(array) + 1)]
    length = 0
    for i, num in enumerate(array):
        new_length = binary_search(1, length, indicies, array, num)
        seqs[i] = indicies[new_length - 1]
        indicies[new_length] = i
        length = max(length, new_length)
    return build_sequence(array, seqs, indicies[length])
    
def binary_search(start, end, indicies, array, num):
    if start > end:
        return start
    middle = (start + end) // 2
    if array[indicies[middle]] < num:
        start = middle + 1
    else:
        end = middle - 1
    return binary_search(start, end, indicies, array, num)

def build_sequence(array, seqs, curr):
    seq = []
    while curr is not None:
        seq.append(array[curr])
        curr = seqs[curr]
    return list(reversed(seq))
