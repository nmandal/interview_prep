# O(N) time | O(1) space
def kadanes_algorithm(array):
    max_here = array[0]
    best = array[0]
    for i in range(1, len(array)):
        max_here = max(array[i], max_here+array[i])
        best = max(max_here, best)
    return best
