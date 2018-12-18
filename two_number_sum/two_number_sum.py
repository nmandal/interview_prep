# Time: O(N) | Space: O(N)
def two_number_sum(array, target_sum):
    num_map = {}
    for num in array:
        potential_match = target_sum - num
        if potential_match in num_map:
            return sorted([potential_match, num])
        num_map[num] = True
    return []
