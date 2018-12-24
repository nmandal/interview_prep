# Upper Bound: O(n^2*n!) time | O(n*n!) space
# Roughly: O(n*n!) time | O(n*n!) space
def permutations(arr):
    if not len(arr):
        return []
    perms = []
    _permutations(arr, [], perms)
    return perms

def _permutations(arr, curr_perm, perms):
    if not len(arr):
        perms.append(curr_perm)
    else:
        for i in range(len(arr)):
            new_arr = arr[:i] + arr[i+1:]
            new_perm = curr_perm + [array[i]]
            _permutations(new_arr, new_perm, perms)
