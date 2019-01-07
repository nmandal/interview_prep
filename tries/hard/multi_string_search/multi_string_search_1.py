# O(bns) time | O(n) space
def multi_string_search(big_string, small_strings):
    return [is_in_big_string(big_string, small_string) for small_string in small_strings]

def is_in_big_string(big_string, small_string):
    for i in range(len(big_string)):
        if i + len(small_string) > len(big_string):
            break
        if is_in_big_string_helper(big_string, small_string, i):
            return True
    return False

def is_in_big_string_helper(big_string, small_string, start):
    left_big = start
    right_big = start + len(small_string) - 1
    left_small = 0
    right_small = len(small_string) - 1
    while left_big <= right_big:
        if (big_string[left_big] != small_string[left_small] or big_string[right_big] != small_string[right_small]):
            return False
        left_big += 1
        right_big -= 1
        left_small += 1
        right_small -= 1
    return True
