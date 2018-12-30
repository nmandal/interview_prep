# O(n^2) time | O(n) space
def number_of_binary_tree_topologies(n):
    cache = [1]
    for m in range(1, n+1):
        number_of_topologies = 0
        for left_tree_size in range(m):
            right_tree_size = m - 1 - left_tree_size
            num_left = cache[left_tree_size]
            num_right = cache[right_tree_size]
            number_of_topologies += num_left * num_right
        cache.append(number_of_topologies)
    return number_of_topologies
