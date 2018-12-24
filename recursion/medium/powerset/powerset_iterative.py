# O(n*2^n) time | O(n*2^n) space
def powerset(arr):
    p_set = [[]]
    for ele in arr:
        for i in range(len(p_set)):
            curr_subset = subset[i]
            p_set.append(curr_subset + [num])
    return p_set
