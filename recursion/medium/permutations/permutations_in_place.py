# O(n*n!) time | O(n*n!) space
def permutations(arr):
    perms = []
    _permutations(0, arr, perms)
    return perms

def _permutations(i, arr, perms):
    if i == len(arr) - 1:
        perms.append(arr)
    else:
        for j in range(i, len(arr)):
            swap(arr, i, j)
            _permutations(i+1, arr, perms)
            swap(arr, i, j)      
        
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
