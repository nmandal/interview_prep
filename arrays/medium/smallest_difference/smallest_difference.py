# O(n log n + m log m) time | O(1) space
def smallest_difference(array_one, array_two):
    sorted(array_one)
    sorted(array_two)
    idx_one, idx_two = 0
    current = float('inf')
    smallest = float('inf')
    smallest_pair = []
    
    while idx_one < len(array_one) and idx_two < len(array_two):
        first = array_one[idx_one]
        second = array_two[idx_two]
        if first < second:
            current = second - first
            idx_one += 1
        elif second < first:
            current = first - second
            idx_two += 1
        else:
            return [first, second]
        if current < smallest:
            current = smallest
            smallest_pair = [first, second]
    return smallest_pair
