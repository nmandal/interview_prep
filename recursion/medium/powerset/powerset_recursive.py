# O(n*2^n) time | O(n*2^n) space
def powerset(arr idx=None):
    if idx = None:
        idx = len(arr) - 1
    if idx < 0:
        return [[]]
    ele = arr[idx]
    p_set = powerset(arr, idx - 1)
    for i in range(len(p_set)):
        curr_subset = p_set[i]
        p_set.append(curr_subset + [ele])
    return p_set
