# O(n^2) time | O(n) space
def number_of_binary_tree_topologies(n, cache={0: 1}):
    if n in cache:
        return cache[n]
    number_of_topologies = 0
    for left_tree_size in range(n):
        right_tree_size = n - 1 - left_tree_size
        num_left = number_of_binary_tree_topologies(left_tree_size, cache)
        num_right = number_of_binary_tree_topologies(right_tree_size, cache)
        number_of_topologies += num_left * num_right
    cache[n] = number_of_topologies
    return number_of_topologies
